from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class CessionPocPmView(db.Model):
    __tablename__ = 'cession_poc_pm_view'

    id = db.Column(db.Integer, primary_key=True)
    cession_operation_id = db.Column(db.Integer)
    cession_operation_date_cession = db.Column(db.Date)
    cession_operation_date_creation = db.Column(db.DateTime)
    cession_operation_numero_bordeau = db.Column(db.String)
    cession_operation_code_banque = db.Column(db.String)
    cession_operation_code_agence = db.Column(db.String)
    cession_operation_montant_global = db.Column(db.Float)
    cession_operation_total_devises = db.Column(db.Float)
    cession_operation_statut = db.Column(db.Integer)
    cession_operation_poc_categorie = db.Column(db.Integer)
    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String)
    poc_numero_agrement = db.Column(db.String)
    pm_denomination = db.Column(db.String)
    pm_centre = db.Column(db.String)
    pm_registre_commerce = db.Column(db.String)
    operation_devise = db.Column(JSONB)