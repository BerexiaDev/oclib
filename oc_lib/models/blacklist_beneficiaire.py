from sqlalchemy.dialects.postgresql import JSONB

from oc_lib.db import db
from oc_lib.repository import Repository


class BlacklistBeneficiaire(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    denomination = db.Column(db.String(120))
    numero_agrement = db.Column(db.String(50))
    date_operation = db.Column(db.DateTime)
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    fullname = db.Column(db.String(240))
    id_documents = db.Column(db.Array(JSONB))

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
    individual_id = db.Column(db.Integer, db.ForeignKey('individual.id'))
