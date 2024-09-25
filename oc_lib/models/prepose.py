from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners

@register_event_listeners
class Prepose(Pp):
    __tablename__ = 'prepose'
    id = db.Column(db.Integer, db.ForeignKey('pp.id'), primary_key=True)
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    poc = db.relationship('Poc', backref='prepose', uselist=False)

    __mapper_args__ = {'polymorphic_identity': 'prepose'}
