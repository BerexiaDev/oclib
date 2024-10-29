from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date
from sqlalchemy.dialects.postgresql import JSONB

class DemandeStatut(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    etape = db.Column(db.Integer) # Avancement
    date_creation = db.Column(db.Date, default=date.today, onupdate=date.today)
    statut_id = db.Column(db.Integer, db.ForeignKey("statut.id"))
    change = db.Column(JSONB)
    
