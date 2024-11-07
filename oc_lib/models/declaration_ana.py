from oc_lib.repository import Repository
from oc_lib.db import db
from datetime import date


class DeclarationAna(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    date_declaration = db.Column(db.Date, default=date.today)
    motif = db.Column(db.String(50))
    motif_manager = db.Column(db.String(50))
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validateurs = db.Column(db.ARRAY(db.String(240)))
    valide_oc = db.Column(db.Boolean, default=False)
    valide_manager_oc = db.Column(db.Boolean, default=False)
    statut = db.Column(db.Integer)
    decision = db.Column(db.Integer)
    
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id", ondelete="SET NULL")) 
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id", ondelete="SET NULL"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id", ondelete= "SET NULL"))