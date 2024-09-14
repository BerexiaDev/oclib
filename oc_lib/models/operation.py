from datetime import datetime
from oc_lib.repository import Repository
from oc_lib.db import db

class Operation(db.Model, Repository):
    __tablename__ = 'operation'
    
    id = db.Column(db.Integer, primary_key=True)

    numero_bordeau = db.Column(db.String(240))
    date_bordeau = db.Column(db.DateTime, default=datetime.utcnow)
    montant_global = db.Column(db.Float, nullable=False, default = 0)
    statut = db.Column(db.Integer, nullable=False, default = 1) # 1 enregistre, 2 annulee

    # Relationships
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    beneficiaire_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    operation_devises = db.relationship("OperationDevise", cascade="all, delete")
    attachments = db.relationship("OperationAttachment")

    type_operation = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "operation", "polymorphic_on": type_operation}
