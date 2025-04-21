from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date


class DemandeOperation(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    statut = db.Column(db.Integer)
    decision = db.Column(db.Integer)
    motif_modif = db.Column(db.String)
    motif_rejet = db.Column(db.String)
    date_creation = db.Column(db.Date, default=date.today, nullable=False)
    date_validation = db.Column(db.Date)
    initiateur = db.Column(db.String(240))
    validateur = db.Column(db.String(240))
    operation_achat_id = db.Column(
        db.Integer, db.ForeignKey("operation_achat.id"))
    operation_vente_id = db.Column(
        db.Integer, db.ForeignKey("operation_vente.id"))
    operation_cession_id = db.Column(
        db.Integer, db.ForeignKey("operation_cession.id"))

    change = db.relationship(
        "Change", backref="demande_operation", lazy=True, uselist=False)
