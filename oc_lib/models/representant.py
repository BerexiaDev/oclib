from oc_lib.models.pp import Pp
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from sqlalchemy.orm import aliased

#TODO: all qualities need date debut + fin RG
@register_event_listeners
@change_statut_pp_pm_listener
class Representant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))

    # One to one
    suppleant = db.relationship(
        "Suppleant",
        backref="representant",
        uselist=False,
        foreign_keys="[Suppleant.representant_id]",
    )
    @staticmethod
    def validate_unique_active_representant(current_representant):
        # Create an alias for Pp
        PpAlias = aliased(Pp)
        # Query the database for any active gerant with the same scd_id
        active_representant = db.session.query(Representant).join(PpAlias).filter(
            Representant.scd_id == current_representant.scd_id,
            PpAlias.statut.in_([True, None]),
            PpAlias.creation_status != 4
        ).first()
        
        if not active_representant:
            return True
        if active_representant != current_representant:

            raise ValueError(
                "There is already an active representant for this Operator."
            )

    def save(self, *args, **kwargs):
        try:
            # Before saving, validate the uniqueness of the active gerant
            self.validate_unique_active_representant(self)
            super(Representant, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving representant: {str(e)}")
            raise ValueError(e)

    __mapper_args__ = {"polymorphic_identity": "representant"}
