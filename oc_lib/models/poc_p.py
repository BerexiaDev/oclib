from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners

@register_event_listeners
class PocP(Pp):
    __tablename__ = 'pocp'
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    # One to one
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))

    __mapper_args__ = {"polymorphic_identity": "poc_p"}
