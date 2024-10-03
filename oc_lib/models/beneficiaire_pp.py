from oc_lib.db import db
from oc_lib.repository import Repository


class BeneficiairePp(db.Model, Repository):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    nom = db.Column(db.String(120))
    prenom = db.Column(db.String(120))
    nature_piece = db.Column( db.String(50))
    numero_piece = db.Column( db.String(50))
    nationalite = db.Column( db.String(120))
    qualite = db.Column(db.Integer, nullable = False)
    is_final = db.Column(db.Boolean, nullable = False, default = False) # pour deferencier beenfeciaire et beneficiare final
