from datetime import datetime
from oc_lib.repository import Repository
from oc_lib.db import db

class OperationCession(db.Model, Repository):
    __tablename__ = 'operation_cession'
    
    id = db.Column(db.Integer, primary_key=True)
    date_cession = db.Column(db.DateTime, nullable=False) # date bordereau
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    numero_bordereau = db.Column(db.String(240), unique=True)
    code_banque = db.Column(db.Integer)
    code_agence = db.Column(db.Integer)

    label_banque = db.Column(db.String(100))
    label_agence = db.Column(db.String(100))
    
    montant_global = db.Column(db.Float, nullable=False, default = 0) # Contre valeur des devises cedées en MAD
    total_devises = db.Column(db.Float, nullable=False, default = 0)  # Sum of all montant_mad from devises
    statut = db.Column(db.Integer, nullable=False, default = 1) # 1 enregistre, 2 annulee

    created_by = db.Column(db.String(240), nullable=False)
    created_by_id = db.Column(db.Integer, nullable=False)
    devise_labels = db.Column(db.String(1000), nullable=False)    

    is_late = db.Column(db.Boolean, nullable=False)
    poc_date_depassement_seuil = db.Column(db.DateTime)

    cancellation_reason = db.Column(db.String(240))
    cancelled_by = db.Column(db.String(240))
    cancelled_by_id = db.Column(db.Integer)
    date_cancellation = db.Column(db.DateTime)
    validated_by = db.Column(db.String(240))
    validated_by_id = db.Column(db.Integer)

    # Relationships
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id')) 
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
    operation_devises = db.relationship("OperationDevise")
    attachments = db.relationship("OperationAttachment")
