from oc_lib.db import db
from oc_lib.models.operation import Operation


class OperationVente(Operation):
    id = db.Column(db.Integer, db.ForeignKey("operation.id"),
                   primary_key=True, nullable=False)

    lien_parente = db.Column(db.String(240))  # dans le cas de PP
    fonction_pp = db.Column(db.String(240))  # dans le cas de PM
    # Si pp dispose d'autorisation
    numero_autorisation = db.Column(db.String(50), nullable=True)

    beneficiaire_final_pp_id = db.Column(
        db.Integer, db.ForeignKey('beneficiaire_pp_final.id'))
    activation_complement_dotation_id = db.Column(
        db.Integer, db.ForeignKey('activation_complement_dotation.id'))

    __mapper_args__ = {"polymorphic_identity": 2}
