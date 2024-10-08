from oc_lib.repository import Repository
from oc_lib.db import db

class DeclarationPm(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    type_pm = db.Column(db.String, nullable=False)
    denomination_pm = db.Column(db.String(100), nullable=False)
    centre_pm = db.Column(db.Integer, nullable=False)
    rc_pm = db.Column(db.Integer, nullable=False)
    denomination_mandataire = db.Column(db.String(100))
    centre_m = db.Column(db.Integer)
    rc_m = db.Column(db.Integer)
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validator = db.Column(db.String)
    date_demande = db.Column(db.Date)
    statut = db.Column(db.Integer)
    decision = db.Column(db.Integer)
    
    
    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id", ondelete="SET NULL"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id", ondelete="SET NULL"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id", ondelete="SET NULL"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id", ondelete="SET NULL"))