from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class CessionOperationView(db.Model):
    __tablename__ = 'operation_cession_view'

    id = db.Column(db.Integer, primary_key=True)
    op_id = db.Column(db.Integer),
    numero_bordereau = db.Column(db.String),
    date_cession = db.Column(db.Date),
    categorie_op = db.Column(db.String),
    pm_raison_sociale = db.Column(db.String),
    pm_registre_commerce = db.Column(db.Integer),
    pm_centre = db.Column(db.Integer),
    categorie_pc = db.Column(db.Integer),
    poc_id = db.Column(db.Integer),
    poc_denomination = db.Column(db.String),
    poc_numero_agrement = db.Column(db.String),
    created_by = db.Column(db.String),
    date_creation = db.Column(db.DateTime),
    code_banque = db.Column(db.String),
    code_agence = db.Column(db.String),
    devise_labels = db.Column(db.String),
    montant_global = db.Column(db.Float),
    total_devises = db.Column(db.Float),
    statut = db.Column(db.Integer)