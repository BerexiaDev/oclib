from oc_lib.db import db
from oc_lib.repository import Repository


class BeneficiairePm(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rc = db.Column(db.Integer, nullable=False)
    centre = db.Column(db.Integer,nullable=False)
    raison_sociale =db.Column(db.String(100))
    solde_disponible = db.Column(db.Float, nullable=False, default=0)
    qualite = db.Column(db.String(10), nullable=False, default='')
    date_solde = db.Column(db.Date, nullable=False)
    nationalite = db.Column(db.String(120), nullable=True)
    idce = db.Column(db.String(50))