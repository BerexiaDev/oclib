from oc_lib.repository import Repository
from oc_lib.db import db

class DeclarationPoc(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))
    poc_addresse = db.Column(db.String(50), nullable=False)
    numero_agrement = db.Column(db.String(50))
    nom_agence = db.Column(db.String(50))
    type_pm = db.Column(db.String)
    date_demande = db.Column(db.Date)
    motif = db.Column(db.String(50))  
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validator = db.Column(db.String)
    date_debut = db.Column(db.Date)
    date_fin = db.Column(db.Date)
    denomination_pm = db.Column(db.String(100), nullable=False)
    centre_pm = db.Column(db.Integer, nullable=False)
    rc_pm = db.Column(db.Integer, nullable=False)
    denomination_mandataire = db.Column(db.String(100))
    centre_m = db.Column(db.Integer)
    rc_m = db.Column(db.Integer)
    date_declaration_m = db.Column(db.Date)
    statut = db.Column(db.Integer)
    decision = db.Column(db.Integer)
    
    