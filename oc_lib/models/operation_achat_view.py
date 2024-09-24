from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class OperationAchatView(db.Model):
    __tablename__ = 'operation_achat_view'

    id = db.Column(db.Integer, primary_key=True)
    op_id = db.Column(db.Integer)
    numero_bordereau = db.Column(db.String)
    date_bordereau = db.Column(db.DateTime)
    categorie_op = db.Column(db.String)
    pm_raison_sociale = db.Column(db.String)
    pm_registre_commerce = db.Column(db.Integer)
    pm_centre = db.Column(db.Integer)
    categorie_pc = db.Column(db.Integer)
    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String)
    poc_numero_agrement = db.Column(db.String)
    created_by = db.Column(db.String)
    date_creation = db.Column(db.DateTime)
    beneficiaire_pm_qualite = db.Column(db.Integer)
    beneficiaire_pp_qualite = db.Column(db.Integer)
    sous_operation_label = db.Column(db.String)
    beneficiaire_pp_nature_piece = db.Column(db.String)
    beneficiaire_pp_numero_piece = db.Column(db.String)
    beneficiaire_pp_nom = db.Column(db.String)
    beneficiaire_pp_prenom = db.Column(db.String)
    beneficiaire_pp_nationalite = db.Column(db.String)
    beneficiaire_pm_registre_commerce = db.Column(db.Integer)
    beneficiaire_pm_centre = db.Column(db.Integer)
    beneficiaire_pm_raison_sociale = db.Column(db.String)
    beneficiaire_pm_idce = db.Column(db.String)
    numero_declaration = db.Column(db.String)
    date_declaration = db.Column(db.Date)
    statut = db.Column(db.Integer)
    devise_labels = db.Column(db.String)
    montant_global = db.Column(db.Float)

