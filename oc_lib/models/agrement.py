from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners

@register_event_listeners
class Agrement(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_delivrance = db.Column(db.Date)
    date_retrait = db.Column(db.Date)
    statut = db.Column(db.Integer)
    detail_statut = db.Column(db.Integer)
    date_debut = db.Column(db.Date)
    date_fin = db.Column(db.Date)
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))

