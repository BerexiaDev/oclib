from datetime import datetime

from oc_lib.db import db
from oc_lib.repository import Repository

class LocalIndividual(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(240))
    last_name = db.Column(db.String(240))
    passport = db.Column(db.ARRAY(db.String(50)))
    cin = db.Column(db.ARRAY(db.String(50)))
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Local Individual {self.first_name} {self.last_name}>'
