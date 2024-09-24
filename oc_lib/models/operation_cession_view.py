from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class OperationCessionView(db.Model):
    __tablename__ = 'operation_cession_view'

    id = db.Column(db.Integer, primary_key=True)
    op_id = db.Column(db.Integer)
    numero_bordereau = db.Column(db.String(240))
    date_cession = db.Column(db.Date)
    categorie_op = db.Column(db.String(50))
    pm_raison_sociale = db.Column(db.String(100))
    pm_registre_commerce = db.Column(db.Integer)
    pm_centre = db.Column(db.Integer)
    categorie_pc = db.Column(db.Integer)
    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String(50))
    poc_numero_agrement = db.Column(db.String(50))
    created_by = db.Column(db.String(240))
    date_creation = db.Column(db.DateTime)
    code_banque = db.Column(db.String(240))
    code_agence = db.Column(db.String(240))
    devise_labels = db.Column(db.String(1000))
    montant_global = db.Column(db.Float)
    total_devises = db.Column(db.Float)
    statut = db.Column(db.Integer)
