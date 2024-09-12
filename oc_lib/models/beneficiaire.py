from oc_lib.db import db
from oc_lib.repository import Repository

class Beneficiaire(db.Model, Repository):
    __tablename__ = "beneficiaire"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    solde_disponible = db.Column(db.Float, nullable=False, default=0)
    qualite = db.Column(db.Integer, nullable=False )

    __mapper_args__ = {'polymorphic_identity': 'beneficiaire', 'polymorphic_on': type}