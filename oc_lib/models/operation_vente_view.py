from oc_lib.db import db
from oc_lib.repository import Repository
from sqlalchemy.dialects.postgresql import JSONB


class OperationVenteView(db.Model, Repository):
    __tablename__ = 'operation_vente_view'

    id = db.Column(db.Integer, primary_key=True)
    op_id = db.Column(db.Integer)
    numero_bordereau = db.Column(db.String(240))
    date_bordereau = db.Column(db.DateTime)
    categorie_op = db.Column(db.String(50))
    pm_registre_commerce = db.Column(db.Integer)
    pm_raison_sociale = db.Column(db.String(100))
    pm_centre = db.Column(db.Integer)
    categorie_pc = db.Column(db.Integer)
    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String(50))
    poc_numero_agrement = db.Column(db.String(50))
    poc_adresse = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.String(240))
    date_creation = db.Column(db.DateTime)
    beneficiaire_pm_qualite = db.Column(db.Integer, nullable=False)
    beneficiaire_pp_qualite = db.Column(db.Integer, nullable=False)
    beneficiaire_final_pp_qualite = db.Column(db.Integer, nullable=False)
    sous_operation_label = db.Column(db.String, nullable=False)
    sous_operation_id = db.Column(db.Integer, nullable=False)
    beneficiaire_pp_id = db.Column(db.Integer, nullable=False)
    beneficiaire_pp_nature_piece = db.Column(db.String(50), nullable=False)
    beneficiaire_pp_numero_piece = db.Column(db.String(50), nullable=False)
    beneficiaire_pp_nom = db.Column(db.String(120), nullable=False)
    beneficiaire_pp_prenom = db.Column(db.String(120), nullable=False)
    beneficiaire_pp_nationalite = db.Column(db.String(120), nullable=True)
    beneficiaire_pp_adresse = db.Column(db.String(120), nullable=True)
    beneficiaire_final_pp_nature_piece = db.Column(
        db.String(50), nullable=False)
    beneficiaire_final_pp_numero_piece = db.Column(
        db.String(50), nullable=False)
    beneficiaire_final_pp_nom = db.Column(db.String(120), nullable=False)
    beneficiaire_final_pp_prenom = db.Column(db.String(120), nullable=False)
    beneficiaire_final_pp_adresse = db.Column(db.String(120), nullable=True)
    beneficiaire_pm_id = db.Column(db.Integer, nullable=False)
    beneficiaire_pm_registre_commerce = db.Column(db.Integer, nullable=False)
    beneficiaire_pm_centre = db.Column(db.Integer, nullable=False)
    beneficiaire_pm_raison_sociale = db.Column(db.String(100))
    beneficiaire_pm_idce = db.Column(db.BigInteger)
    # Si pp dispose d'autorisation
    numero_autorisation = db.Column(db.String(50), nullable=True)
    statut = db.Column(db.Integer)
    devise_labels = db.Column(db.String(1000))
    montant_global = db.Column(db.Float)
    support_mad = db.Column(JSONB, nullable=False)

    beneficiaire_pc_id = db.Column(db.Integer, nullable=False)
    beneficiaire_pc_numero_agrement = db.Column(db.String(50))
    beneficiaire_pc_nom_agence = db.Column(db.String(50))
    beneficiaire_pc_qualite = db.Column(db.Integer, nullable=False)

    cancellation_reason = db.Column(db.String(240))
    cancelled_by = db.Column(db.String(240))
    date_cancellation = db.Column(db.DateTime)

    activation_complement_dotation_id = db.Column(db.Integer)
    validated_by = db.Column(db.String(240))

    # operation_vente_lien_parente = db.Column(db.String(240)) # dans le cas de PP
    # operation_vente_fonction_pp = db.Column(db.String(240)) # dans le cas de PM
