from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime

class Solde(db.Model, Repository):
    __tablename__ = 'solde'
    
    id = db.Column(db.Integer, primary_key=True)
    montant = db.Column(db.Float, nullable=False, default=0)
    date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    beneficiaire_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))    
