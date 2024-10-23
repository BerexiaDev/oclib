from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from sqlalchemy.orm import aliased

@register_event_listeners
@change_statut_pp_pm_listener
class Suppleant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    representant_id = db.Column(db.Integer, db.ForeignKey("representant.id"))
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))

    @staticmethod
    def validate_unique_active_suppleant(current_suppleant):
        # Create an alias for Pp
        PpAlias = aliased(Pp)
        # Query the database for any active gerant with the same scd_id
        active_suppleant = db.session.query(Suppleant).join(PpAlias).filter(
            Suppleant.scd_id == current_suppleant.scd_id,
            PpAlias.statut.in_([True, None]),
            PpAlias.creation_status != 4
        ).first()
        
        if not active_suppleant:
            return True
        
        if active_suppleant != current_suppleant:

            raise ValueError(
                "There is already an active suppleant for this Operator."
            )

    def save(self, *args, **kwargs):
        try:
            # Before saving, validate the uniqueness of the active gerant
            self.validate_unique_active_suppleant(self)
            super(Suppleant, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving suppleant: {str(e)}")
            raise ValueError(e)

    __mapper_args__ = {"polymorphic_identity": "suppleant"}