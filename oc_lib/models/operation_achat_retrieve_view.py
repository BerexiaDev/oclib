from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class OperationAchatRetrieveView(db.Model):
    __tablename__ = 'operation_achat_retrieve_view'

    operation_id = db.Column(db.Integer, primary_key=True)
    operation_numero_bordeau = db.Column(db.String(240))
    operation_date_bordeau = db.Column(db.DateTime)
    scd_id = db.Column(db.Integer)
    esd_id = db.Column(db.Integer)
    ep_id = db.Column(db.Integer)
    mandataire_id = db.Column(db.Integer)
    b_pm_registre_commerce = db.Column(db.Integer)
    b_pm_centre = db.Column(db.Integer)
    b_pm_raison_sociale = db.Column(db.String(100))
    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String(255))
    po_numero_agrement = db.Column(db.String(50))
    sous_operation_type = db.Column(Integer)
    qualite = db.Column(db.Integer)
    beneficiaire_nom = db.Column(db.String(120))
    beneficiaire_prenom = db.Column(db.String(120))
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    nationalite = db.Column(db.String(120))
    ice = db.Column(db.String(50))
    count_of_devises = db.Column(db.Integer)
    montant_global = db.Column(db.Float)
    op_statut = db.Column(db.Integer)
    devises = db.Column(JSONB)
