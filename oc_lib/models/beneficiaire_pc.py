from oc_lib.db import db
from oc_lib.repository import Repository

class BeneficiairePc(db.Model, Repository):
    id = db.Column( db.Integer, primary_key=True )
    poc_id = db.Column( db.Integer, nullable=False )
    numero_agrement = db.Column(db.String(50))
    nom_agence = db.Column(db.String(50))
    qualite = db.Column(db.Integer, nullable=False)
