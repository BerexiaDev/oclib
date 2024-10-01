from oc_lib.db import db
from oc_lib.models.pp import Pm
from oc_lib.utils.events_decorator import register_event_listeners

@register_event_listeners
class CogerantPm(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    __mapper_args__ = {"polymorphic_identity": "cogerantpm"}