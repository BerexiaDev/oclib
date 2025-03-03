from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime


class PaimentModes(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)