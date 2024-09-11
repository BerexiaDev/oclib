from oc_lib.db import db
from oc_lib.models.autorisation_particuliere import AutorisationParticuliere

class AutorisationParticulierePM(AutorisationParticuliere):
    id = db.Column(db.Integer, db.ForeignKey("autorisation_particuliere.id"), primary_key=True, nullable=False)
    #Many to one
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    beneficiaire_pm = db.relationship("BeneficiairePM")

    __mapper_args__ = {'polymorphic_identity': 'autorisation_particuliere_pm'}