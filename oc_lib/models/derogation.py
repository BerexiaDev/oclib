from sqlalchemy.orm import validates

from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.validators import validate_numero_decision


class Derogation(db.Model, Repository):
    __tablename__ = "derogation"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    numero_decision = db.Column(db.String, nullable=False)
    date_decision = db.Column(db.Date, nullable=False)
    created_by = db.Column(db.String(240), nullable=False)
    statut = db.Column(db.Integer, default=1) # 1 == encours
    validated_by = db.Column(db.String(240))

    __mapper_args__ = {'polymorphic_identity': 'derogation', 'polymorphic_on': type}

    @validates('numero_decision')
    def validate_numero_decision_value(self, key, value):
        return validate_numero_decision(key, value)
