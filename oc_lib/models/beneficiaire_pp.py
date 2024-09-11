from oc_lib.db import db
from oc_lib.models.beneficiaire import Beneficiaire

class BeneficiairePp(Beneficiaire):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire.id"), primary_key=True, nullable=False)
    nom = db.Column(db.String(120),nullable=False)
    prenom = db.Column(db.String(120),nullable=False)
    nature_piece_identite = db.Column(db.String(50),nullable=False)
    numero_piece_identite = db.Column(db.String(50),nullable=False)
    nationalite = db.Column(db.String(120),nullable=False)
    
    __mapper_args__ = {'polymorphic_identity': 'beneficiaire_pp'}