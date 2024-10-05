from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime

class ActivationComplementDotation(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    complement_dotation_id = db.Column(db.Integer, db.ForeignKey('complement_dotation.id'))
    beneficiaire_pp_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pp.id'))
    beneficiaire_pm_id = db.Column(db.Integer, db.ForeignKey('beneficiaire_pm.id'))
    date_activation = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    nature_document = db.Column(db.String(100), nullable = False)
    adminitration_emettrice = db.Column(db.String(100), nullable = False)
    nom_document = db.Column(db.String(100), nullable = True)
    path_document = db.Column(db.String(100), nullable = True)