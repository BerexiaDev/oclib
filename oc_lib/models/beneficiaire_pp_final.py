from oc_lib.db import db
from oc_lib.models.beneficiaire_pp import BeneficiairePp


class BeneficiairePpFinal(BeneficiairePp):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire_pp.id"),
                   primary_key=True, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "beneficiaire_pp_final"}
