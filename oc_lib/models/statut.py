from datetime import datetime
from sqlalchemy.orm import validates

from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners
from oc_lib.utils.validators import validate_numero_decision


@register_event_listeners
class Statut(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.Integer, default=0)
    statut_activite = db.Column(db.Integer, nullable=False)
    statut_agrement = db.Column(db.Integer, nullable=False)
    next_statut_activite = db.Column(db.Integer)
    next_statut_agrement = db.Column(db.Integer)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date)
    commentaire = db.Column(db.String)
    numero_decision = db.Column(db.String)
    date_decision = db.Column(db.Date)
    date_delivrance = db.Column(db.Date)
    numero_delivrance = db.Column(db.String(50))
    avancement = db.Column(db.Integer, default=0)
    is_valid = db.Column(db.Boolean, default=True)
    date_avancement = db.Column(db.Date, default=datetime.utcnow, onupdate=datetime.utcnow)

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    __mapper_args__ = {'polymorphic_identity': 'statut'}

    @validates('numero_decision')
    def validate_numero_decision_value(self, key, value):
        return validate_numero_decision(key, value)
