from oc_lib.db import db
from oc_lib.repository import Repository

class OperationDevise(db.Model, Repository):
    __tablename__ = 'operation_devise'
    
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100), nullable=False)
    montant_devise = db.Column(db.Float)
    cours = db.Column(db.Float)
    montant_mad = db.Column(db.Float)
    support = db.Column(db.Integer)
    
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))