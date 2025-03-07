from oc_lib.repository import Repository
from oc_lib.db import db
from datetime import datetime

class DeclarationPm(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    type_pm = db.Column(db.String, nullable=False)
    denomination_pm = db.Column(db.String(100), nullable=False)
    centre_pm = db.Column(db.Integer, nullable=False)
    rc_pm = db.Column(db.Integer, nullable=False)
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validator = db.Column(db.String)
    date_demande = db.Column(db.DateTime, default=datetime.today)
    statut = db.Column(db.Integer) # Avancement
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    motif = db.Column(db.String)
    
    
    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id", ondelete="SET NULL"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id", ondelete="SET NULL"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id", ondelete="SET NULL"))
