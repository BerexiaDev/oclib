from oc_lib.db import db
from oc_lib.models.beneficiaire import Beneficiaire

class BeneficiairePM(Beneficiaire):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire.id"), primary_key=True, nullable=False)

    rc = db.Column(db.String(100))
    centre = db.Column(db.String(100))
    saison_sociale =db.Column(db.String(100))

    __mapper_args__ = {'polymorphic_identity': 'beneficiaire_pm'}