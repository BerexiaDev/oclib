from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from oc_lib.utils.db_utils import validate_unique_active

@register_event_listeners
@change_statut_pp_pm_listener
class Suppleant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    representant_id = db.Column(db.Integer, db.ForeignKey("representant.id"))
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))

    @staticmethod
    def validate_wrapper(self):
        validate_unique_active(Suppleant, self)

    def save(self, *args, **kwargs):
        try:
            # Before saving, validate the uniqueness of the active gerant
            self.validate_wrapper(self)
            super(Suppleant, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving suppleant: {str(e)}")
            raise ValueError(e)

    __mapper_args__ = {"polymorphic_identity": "suppleant"}