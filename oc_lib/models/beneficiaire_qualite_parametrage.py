from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime

class BeneficiaireQualiteParameterage(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
