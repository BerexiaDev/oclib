from sqlalchemy.orm import validates

from oc_lib.db import db
from oc_lib.models.beneficiaire import Beneficiaire
from oc_lib.utils.validators import validate_numero_piece


class BeneficiairePp(Beneficiaire):
    id = db.Column(db.Integer, db.ForeignKey("beneficiaire.id"),
                   primary_key=True, nullable=False)
    nom = db.Column(db.String(120))
    prenom = db.Column(db.String(120))
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "beneficiaire_pp"}

    @validates('numero_piece')
    def validate_numero_piece_value(self, key, value):
        return validate_numero_piece(key, value)
