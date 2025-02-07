from oc_lib.db import db
from oc_lib.repository import Repository

class OperationDevise(db.Model, Repository):
    __tablename__ = 'operation_devise'
    
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    montant_devise = db.Column(db.Float)
    cours = db.Column(db.Float)
    montant_mad = db.Column(db.Float)
    support = db.Column(db.Integer)
    solde_de_depart = db.Column(db.Float)
    
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
    operation_cession_id = db.Column(db.Integer, db.ForeignKey('operation_cession.id'))
