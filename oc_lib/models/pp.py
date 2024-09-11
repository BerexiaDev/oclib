from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners


class Pp(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    nationalite = db.Column(db.String(50))
    adresse = db.Column(db.String(100))
    email = db.Column(db.String)
    phone = db.Column(db.String)
    nature_pp = db.Column(db.String(50))
    type = db.Column(db.String(50))
    date_nomination = db.Column(db.Date, nullable=False, default=db.func.now())     # date appointment
    date_demission = db.Column(db.Date)      # date resignation

    __mapper_args__ = {'polymorphic_identity': 'pp', 'polymorphic_on': type}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        register_event_listeners(type(self))
