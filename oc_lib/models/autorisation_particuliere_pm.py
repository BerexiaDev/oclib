from oc_lib.db import db
from oc_lib.models.autorisation_particuliere import AutorisationParticuliere

class AutorisationParticulierePm(AutorisationParticuliere):

    id = db.Column(db.Integer, db.ForeignKey("autorisation_particuliere.id"), primary_key=True, nullable=False)
    date_debut_effet = db.Column(db.Date, nullable=True)
    date_fin_effet = db.Column(db.Date, nullable=True)

    #Many to one
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    beneficiaire_pm = db.relationship("BeneficiairePm")

    __mapper_args__ = {'polymorphic_identity': 'autorisation_particuliere_pm'}