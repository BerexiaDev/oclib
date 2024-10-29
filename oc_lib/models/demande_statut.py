from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date

class DemandeStatut(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    etape = db.Column(db.Integer) # Avancement

    statut_id = db.Column(db.Integer, db.ForeignKey("statut.id"))
    
