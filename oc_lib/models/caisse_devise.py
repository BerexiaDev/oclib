from oc_lib.db import db
from oc_lib.repository import Repository

class CaisseDevise(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(240))  # A poc shouldn't have duplicated currencies
    montant = db.Column(db.Float)

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
