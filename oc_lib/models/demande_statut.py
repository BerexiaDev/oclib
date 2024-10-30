from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date
from sqlalchemy.dialects.postgresql import JSONB

class DemandeStatut(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    etape = db.Column(db.Integer) # Avancement
    state = db.Column(db.Integer)
    categorie_pc = db.Column(db.Integer)
    numero_agrement = db.Column(db.String(50))
    rs_pm = db.Column(db.String)
    categorie_pm = db.Column(db.Integer)
    statut_activite = db.Column(db.Integer)
    statut_agrement = db.Column(db.Integer)
    new_statut_activite = db.Column(db.Integer)
    date_debut_activite = db.Column(db.Date)
    date_fin_activite = db.Column(db.Date)
    numero_decision = db.Column(db.String)
    date_decision = db.Column(db.Date)
    commentaire = db.Column(db.String)
    motif = db.Column(db.String(150))
    initiateur = db.Column(db.String(150))
    validateur = db.Column(db.String(150))
    date_creation = db.Column(db.Date, default=date.today, onupdate=date.today)
    statut_id = db.Column(db.Integer, db.ForeignKey("statut.id"))
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))
    change = db.Column(JSONB)
    
