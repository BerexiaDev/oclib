from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from sqlalchemy.orm import validates

@register_event_listeners
@change_statut_pp_pm_listener
class Cogerant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)

    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))

    @validates("address")
    def validate_address(self, key, address):
        if not address:
            raise ValueError("L'adress est obligatoir pour un cogerant.")
        return address

    __mapper_args__ = {"polymorphic_identity": "cogerant"}
