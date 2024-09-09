from oc_lib.repository import Repository
from oc_lib.db import db

class Motif(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    motif = db.Column(db.Integer, nullable=False)
    date_debut = db.Column(db.Date, nullable=False)
    date_fin = db.Column(db.Date)
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))

