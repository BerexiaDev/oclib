from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.constants import Roles


class Operation(db.Model, Repository):
    __tablename__ = 'operation'
    ROLES_FOR_EXPORT = [Roles.OC_SUPER_ADMIN.value, Roles.OC_ADMIN.value, Roles.OC_AGENT.value, Roles.OC_MANAGER.value]
    
    id = db.Column(db.Integer, primary_key=True)

    numero_bordereau = db.Column(db.String(240))
    date_bordereau = db.Column(db.DateTime, default=datetime.utcnow)
    montant_global = db.Column(db.Float, nullable=False, default = 0)
    support_mad = db.Column(JSONB, nullable=False)

    statut = db.Column(db.Integer, nullable=False, default = 1) # 1 enregistre, 2 annulee

    # Relationships
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    beneficiaire_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
    operation_devises = db.relationship("OperationDevise", cascade="all, delete")
    attachments = db.relationship("OperationAttachment")

    type_operation = db.Column(db.String(50), nullable=False)
    beneficiaire_pp = db.relationship("BeneficiairePp", backref="operation")
    beneficiaire_pm = db.relationship("BeneficiairePm", backref="operation")
    nom = db.Column(db.String(120))
    prenom = db.Column(db.String(120))
    raison_sociale =db.Column(db.String(100))
    
    created_by = db.Column(db.String(240), nullable=False)
    created_by_id = db.Column(db.Integer, nullable=False)
    devise_labels = db.Column(db.String(1000), nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
 
    __mapper_args__ = {"polymorphic_identity": "operation", "polymorphic_on": type_operation}
