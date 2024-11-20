from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date


class Demande(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    decision = db.Column(db.Integer) # Statut (accepté/rejeté)
    statut = db.Column(db.Integer) # Avancement
    etape = db.Column(db.Integer)
    motif_oc_decision = db.Column(db.String)
    motif = db.Column(db.String)
    initiateur = db.Column(db.Integer)
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validateurs = db.Column(db.ARRAY(db.String(240)))
    valide_oc = db.Column(db.Boolean, default=False)
    valide_manager_oc = db.Column(db.Boolean, default=False)
    date_creation = db.Column(db.Date, default=date.today, onupdate=date.today)
    modification_id = db.Column(db.Integer, db.ForeignKey('modification.id'))
    modification = db.relationship('Modification', back_populates='demandes', lazy=True)
    
    change = db.relationship("Change", backref="demande", lazy=True, uselist=False)
    ep = db.Column(db.Integer, db.ForeignKey("ep.id"))
    scd = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd = db.Column(db.Integer, db.ForeignKey("esd.id"))

    denomination_pm = db.Column(db.String(255), nullable=False)
    centre_pm = db.Column(db.Integer, nullable=False)
    rc_pm = db.Column(db.Integer, nullable=False)
    type_pm = db.Column(db.String, nullable=False)

    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)
