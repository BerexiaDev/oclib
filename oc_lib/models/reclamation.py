from datetime import date
from sqlalchemy.orm import validates

from oc_lib.utils.validators import validate_numero_decision
from oc_lib.db import db
from oc_lib.repository import Repository


class Reclamation(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    solde = db.Column(db.Float, nullable=False)
    statut = db.Column(db.Integer)
    commentaire = db.Column(db.String(240))

    poc_id = db.Column(db.Integer)
    poc_denomination = db.Column(db.String(50))

    beneficiaire_pp_id = db.Column(db.Integer)
    beneficiaire_pp_nature_piece = db.Column(db.String(50))
    beneficiaire_pp_numero_piece = db.Column(db.String(50))
    beneficiaire_pp_nom = db.Column(db.String(120))
    beneficiaire_pp_prenom = db.Column(db.String(120))

    beneficiaire_pm_id = db.Column(db.Integer)
    beneficiaire_pm_registre_commerce = db.Column(db.Integer)
    beneficiaire_pm_centre = db.Column(db.Integer)
    beneficiaire_pm_raison_sociale = db.Column(db.String(100))

    processed_by = db.Column(db.String(240))
    date_processed = db.Column(db.Date, nullable=True)

    sous_operation_id = db.Column(
        db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
