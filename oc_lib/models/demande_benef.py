from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date

class DemandeBenef(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    statut = db.Column(db.Integer) # Avancement (encours de validation, traité)
    motif = db.Column(db.String)

    initiateur = db.Column(db.Integer)
    created_by = db.Column(db.String(240), nullable=False)
    validateur = db.Column(db.String(240))
    valide_manager_oc = db.Column(db.Boolean, default=False)
    benef_pp_id = db.Column(db.Integer, db.ForeignKey("beneficiaire_pp.id"))
    benef_pm_id = db.Column(db.Integer, db.ForeignKey("beneficiaire_pm.id"))
    date_creation = db.Column(db.Date, default=date.today, onupdate=date.today)

    change = db.relationship("Change", backref="demande_benef", lazy=True, uselist=False)
