from oc_lib.db import db
from oc_lib.repository import Repository


class BeneficiairePm(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    registre_commerce = db.Column(db.Integer)
    centre = db.Column(db.Integer)
    raison_sociale =db.Column(db.String(100))
    qualite = db.Column(db.Integer, nullable=False)
    nationalite = db.Column(db.String(120), nullable=True)
    idce = db.Column(db.String(50))