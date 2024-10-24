from oc_lib.models.pp import Pp
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from oc_lib.utils.db_utils import validate_unique_active

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
    def validate_wrapper(self):
        validate_unique_active(Representant, self)

    def save(self, *args, **kwargs):
        try:
            # Before saving, validate the uniqueness of the active gerant
            self.validate_wrapper(self)
            super(Representant, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving representant: {str(e)}")
            raise ValueError(e)

    __mapper_args__ = {"polymorphic_identity": "representant"}
