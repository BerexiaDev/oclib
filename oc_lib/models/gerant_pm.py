from oc_lib.db import db
from app.db.pm import Pm
from app.main.utils.events_decorator import register_event_listeners

@register_event_listeners
class GerantPm(Pm):
    id = db.Column(db.Integer, db.ForeignKey('pm.id'), primary_key=True)

    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))

    __mapper_args__ = {'polymorphic_identity': 'gerantpm'}
