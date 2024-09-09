from oc_lib.repository import Repository
from oc_lib.db import db


class Derogation(db.Model, Repository):
    __tablename__ = "derogation"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    numero_decision = db.Column(db.String, nullable=False)
    date_decision = db.Column(db.Date, nullable=False)
    created_by = db.Column(db.String(240), nullable=False)
    statut = db.Column(db.Integer, default=1) # 1 == encours
    validator = db.Column(db.String)

    __mapper_args__ = {'polymorphic_identity': 'derogation', 'polymorphic_on': type}

