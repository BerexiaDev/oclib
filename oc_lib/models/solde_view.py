from oc_lib.db import db
from oc_lib.repository import Repository
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime

class SoldeView(db.Model, Repository): 
    __tablename__ = 'solde_view'

    id = db.Column(db.Integer, primary_key=True)
    solde_id = db.Column(db.Integer)
    solde_montant = db.Column(db.Float, nullable=False, default=0)
    solde_date = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    sous_operation_label = db.Column(db.String, nullable=False)
    type_operation = db.Column(db.Integer, nullable=False)
    activation_complement_dotation_montant = db.Column(db.Float, nullable = False)
    activation_complement_dotation_date_activation = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    autorisation_particuliere_montant_supplementaire = db.Column(db.Float, nullable=False, default=0)
    autorisation_particuliere_numero_autorisation = db.Column(db.String(50), nullable=False)
    beneficiaire_id = db.Column(db.Integer)