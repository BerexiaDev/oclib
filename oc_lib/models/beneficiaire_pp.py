from oc_lib.db import db
from oc_lib.repository import Repository


class BeneficiairePp(db.Model, Repository):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(120), nullable=False)
    prenom = db.Column(db.String(120), nullable=False)
    nature_piece = db.Column(db.String(50), nullable=False)
    numero_piece = db.Column(db.String(50), nullable=False)
    nationalite = db.Column(db.String(120), nullable=True)
    solde_disponible = db.Column(db.Float, nullable=False, default=0)
    qualite = db.Column(db.Integer, nullable=False)
    date_solde = db.Column(db.Date, nullable=False)
    is_final = db.Column(db.Boolean, nullable=False, default=False) # pour deferencier beenfeciaire et beneficiare final