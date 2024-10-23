from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from sqlalchemy.orm import aliased

@register_event_listeners
@change_statut_pp_pm_listener
class Gerant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)

    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))
    
    @staticmethod
    def validate_unique_active_gerant(current_gerant):
        # Create an alias for Pp
        PpAlias = aliased(Pp)
        # Query the database for any active gerant with the same scd_id
        active_gerant = db.session.query(Gerant).join(PpAlias).filter(
            Gerant.scd_id == current_gerant.scd_id if current_gerant.scd_id else Gerant.esd_id == current_gerant.esd_id,
            PpAlias.statut.in_([True, None]),
            PpAlias.creation_status != 4
        ).first()
        
        if not active_gerant:
            return True
        if active_gerant:

            raise ValueError(
                "There is already an active gerant for this Operator."
            )

    def save(self, *args, **kwargs):
        try:
            # Before saving, validate the uniqueness of the active gerant
            self.validate_unique_active_gerant(self)
            super(Gerant, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving Gerant: {str(e)}")
            raise ValueError(e)

    __mapper_args__ = {"polymorphic_identity": "gerant"}