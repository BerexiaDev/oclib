from oc_lib.db import db
from oc_lib.repository import Repository

class BeneficiairePm(db.Model, Repository):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rc = db.Column(db.String(100))
    centre = db.Column(db.String(100))
    raison_sociale =db.Column(db.String(100))
    solde_disponible = db.Column(db.Float, nullable=False, default=0)
    qualite = db.Column(db.Integer, nullable=False )