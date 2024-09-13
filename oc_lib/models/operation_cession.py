from datetime import datetime
from oc_lib.repository import Repository
from oc_lib.db import db

class OperationCession(db.Model, Repository):
    __tablename__ = 'operation_cession'
    
    id = db.Column(db.Integer, primary_key=True)
    date_cession = db.Column(db.Date, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)  
    numero_bordeau = db.Column(db.String(240))
    code_banque = db.Column(db.String(240))
    code_agence = db.Column(db.String(240))
    
    montant_global = db.Column(db.Float, nullable=False, default = 0) # Contre valeur des devises cedées en MAD
    total_devises = db.Column(db.Float, nullable=False, default = 0)  # Sum of all montant_mad from devises
    statut = db.Column(db.Integer, nullable=False, default = 1) # 1 enregistre, 2 annulee

    # Relationships
    operation_devises = db.relationship("OperationDevise", back_populates="operation_cession")
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id')) 