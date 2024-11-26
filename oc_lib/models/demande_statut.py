from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date
from sqlalchemy.dialects.postgresql import JSONB

class DemandeStatut(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    etape = db.Column(db.Integer) # Avancement
    state = db.Column(db.Integer)
    rs_pm = db.Column(db.String)
    categorie_pm = db.Column(db.Integer)
    motif = db.Column(db.String(150))
    initiateur = db.Column(db.String(150))
    validateur = db.Column(db.String(150))
    date_creation = db.Column(db.Date, default=date.today)
    statut_id = db.Column(db.Integer, db.ForeignKey("statut.id"))
    statut = db.relationship("Statut", backref="demande_statut", lazy=True, uselist=False)
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))
    poc = db.relationship("Poc", backref="demande_statut", lazy=True, uselist=False)
    change = db.Column(JSONB)
    
