from sqlalchemy.dialects.postgresql import JSONB

from oc_lib.db import db
from oc_lib.repository import Repository


class BlacklistBeneficiaire(db.Model, Repository):
    __tablename__ = 'blacklist_beneficiaire'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    denomination = db.Column(db.String(120))
    numero_agrement = db.Column(db.String(50))
    date_operation = db.Column(db.DateTime, nullable=False)
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    fullname = db.Column(db.String(240))
    id_documents = db.Column(JSONB)
    individual_type = db.Column(db.String(50), nullable=False)
    individual_id = db.Column(db.Integer, nullable=False)

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'), nullable=False)
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'), nullable=False)
