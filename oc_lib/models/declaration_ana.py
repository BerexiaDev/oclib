from oc_lib.repository import Repository
from oc_lib.db import db
from datetime import date


class DeclarationAna(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    nom_agence = db.Column(db.String(50))
    adresse = db.Column(db.String(50), nullable=False)
    localite = db.Column(db.String(50), nullable=False)
    localite_code = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    is_agrement = db.Column(db.Boolean, default=False)
    numero_agrement = db.Column(db.String(50))
    seuil_encaisse = db.Column(db.Float)
    date_debut_activite = db.Column(db.Date, nullable=False)
    statut_activite = db.Column(db.Integer, default=1) #En activité par défaut
    statut_agrement = db.Column(db.Integer, default=3) #Neant par défaut
    date_debut_statut = db.Column(db.Date)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    nature_prepose = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    nationalite = db.Column(db.String(50))
    adresse_prepose = db.Column(db.String(100))
    email = db.Column(db.String)
    phone = db.Column(db.String)
    date_nomination = db.Column(db.Date) 
    type_pm = db.Column(db.String)
    date_declaration = db.Column(db.Date, default=date.today)
    motif = db.Column(db.String(50)) 
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validator = db.Column(db.String)
    statut = db.Column(db.Integer)
    decision = db.Column(db.Integer)
    
    # One to one
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id", ondelete="SET NULL"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id", ondelete= "SET NULL"))
    
    lieu_implantation_id = db.Column(db.Integer, db.ForeignKey("lieu_implantation.id"))
    lieu_implantation = db.relationship("LieuImplantation", backref="declaration_ana")