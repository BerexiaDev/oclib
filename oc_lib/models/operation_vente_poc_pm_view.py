from oc_lib.db import db

class OperationVentePocPmView(db.Model):
    __tablename__ = 'operation_vente_poc_pm_view'

    id = db.Column(db.Integer, primary_key=True)
    operation_vente_id = db.Column(db.Integer)
    operation_vente_numero_bordereau = db.Column(db.String(240))
    operation_vente_date_bordereau = db.Column(db.DateTime)
    operation_vente_statut = db.Column(db.Integer)
    operation_vente_montant_global = db.Column(db.Float)
    operation_vente_created_by = db.Column(db.String(240))
    operation_vente_date_creation = db.Column(db.DateTime)
    
    operation_vente_lien_parente = db.Column(db.String(240)) # dans le cas de PP
    operation_vente_fonction_pp = db.Column(db.String(240)) # dans le cas de PM
    operation_vente_numero_autorisation = db.Column(db.String(240), nullable=True) # Si pp dispose d'autorisation 
    
    poc_scd_id = db.Column(db.Integer, nullable=True)
    poc_ep_id = db.Column(db.Integer, nullable=True)
    poc_esd_id = db.Column(db.Integer, nullable=True)
    poc_mandataire_id = db.Column(db.Integer, nullable=True)
    poc_nom_agence = db.Column(db.String(50))
    poc_is_agrement =  db.Column(db.Boolean)
    
    pm_registre_commerce = db.Column(db.Integer)
    pm_raison_sociale =  db.Column(db.String(100))
    pm_centre = db.Column(db.Integer)
    
    beneficiaire_pm_id=  db.Column(db.Integer, nullable=False)
    beneficiaire_pm_qualite =  db.Column(db.Integer, nullable=False)
    beneficiaire_pm_registre_commerce = db.Column(db.Integer, nullable=False)
    beneficiaire_pm_centre = db.Column(db.Integer, nullable=False)
    beneficiaire_pm_raison_sociale = db.Column(db.String(100))
    beneficiaire_pm_idce = db.Column(db.String(50))
    
    beneficiaire_pp_id = db.Column(db.Integer, nullable=False)
    beneficiaire_pp_qualite = db.Column(db.Integer, nullable=False)
    beneficiaire_pp_nom = db.Column(db.String(120), nullable=False)
    beneficiaire_pp_prenom = db.Column(db.String(120), nullable=False)
    beneficiaire_pp_nature_piece = db.Column( db.String(50), nullable=False )
    beneficiaire_pp_numero_piece = db.Column( db.String(50), nullable=False )
    
    beneficiaire_final_pp_id = db.Column(db.Integer, nullable=False)
    beneficiaire_final_pp_qualite = db.Column(db.Integer, nullable=False)
    beneficiaire_final_pp_nom = db.Column(db.String(120), nullable=False)
    beneficiaire_final_pp_prenom_beneficiaire_final_pp = db.Column(db.String(120), nullable=False)
    beneficiaire_final_pp_nature_piece = db.Column( db.String(50), nullable=False )
    beneficiaire_final_pp_numero_piece = db.Column( db.String(50), nullable=False )
    
    
    
    sous_operation_label = db.Column(db.String, nullable=False)