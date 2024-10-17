from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime

class ActivationComplementDotation(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    complement_dotation_id = db.Column(db.Integer, db.ForeignKey('complement_dotation.id'))
    beneficiaire_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    date_activation = db.Column(db.DateTime(timezone=True), nullable = False, default = datetime.utcnow)
    montant = db.Column(db.Float, nullable = False)
    montant_base = db.Column(db.Float, nullable = False)
    nature_document = db.Column(db.String(100), nullable = False)
    adminitration_emettrice = db.Column(db.String(100), nullable = False)
    nom_document = db.Column(db.String(500), nullable = True)
    path_document = db.Column(db.String(500), nullable = True)
    file_extension = db.Column(db.String(5), nullable = True)
    