from datetime import date
from oc_lib.db import db
from oc_lib.repository import Repository

class DemandeAnnulation(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    statut = db.Column(db.Integer)
    decision_final = db.Column(db.Boolean)
    initiateur = db.Column(db.String)
    motif = db.Column(db.Text)
    validateur = db.Column(db.String)
    date_creation = db.Column(db.Date, default=date.today)
    date_validation = db.Column(db.Date)

    #one to one relationship
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
    operation_cession_id = db.Column(db.Integer, db.ForeignKey('operation_cession.id'))