from oc_lib.db import db
from oc_lib.repository import Repository


class BeneficiairePp(Beneficiaire):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire.id"), primary_key=True, nullable=False)
    nom = db.Column(db.String(120))
    prenom = db.Column(db.String(120))
    nature_piece = db.Column( db.String(50))
    numero_piece = db.Column( db.String(50))
    is_final = db.Column(db.Boolean, nullable=False, default=False) # pour deferencier beenfeciaire et beneficiare final

    __mapper_args__ = {"polymorphic_identity": "beneficiaire_pp"}
