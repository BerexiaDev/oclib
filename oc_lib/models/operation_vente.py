from oc_lib.db import db
from oc_lib.models.operation import Operation

class OperationVente(Operation):
    id = db.Column(db.Integer, db.ForeignKey("operation.id"), primary_key=True, nullable=False)

    lien_parente = db.Column(db.String(240)) # dans le cas de PP
    fonction_pp = db.Column(db.String(240)) # dans le cas de PM
    numero_autorisation = db.Column(db.String(240), nullable=True) # Si pp dispose d'autorisation 

    beneficiaire_final_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))

    __mapper_args__ = {"polymorphic_identity": "vente"}