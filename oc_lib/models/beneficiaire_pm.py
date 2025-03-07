from oc_lib.db import db
from oc_lib.repository import Repository
from oc_lib.models.beneficiaire import Beneficiaire


class BeneficiairePm(Beneficiaire):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire.id"), primary_key=True, nullable=False)
    registre_commerce = db.Column(db.Integer)
    centre = db.Column(db.Integer)
    raison_sociale =db.Column(db.String(100))
    id_pays = db.Column( db.String(120))
    idce = db.Column(db.BigInteger)

    __mapper_args__ = {"polymorphic_identity": "beneficiaire_pm"}
