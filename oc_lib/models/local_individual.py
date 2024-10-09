from datetime import datetime

from oc_lib.db import db
from oc_lib.repository import Repository

class LocalIndividual(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    passport = db.Column(db.Array(db.String))
    cin = db.Column(db.Array(db.String))
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Local Individual {self.first_name} {self.last_name}>'
