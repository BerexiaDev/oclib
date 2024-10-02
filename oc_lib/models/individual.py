from datetime import datetime

from oc_lib.db import db
from oc_lib.repository import Repository

class Individual(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    second_name = db.Column(db.String)
    third_name = db.Column(db.String)
    fourth_name = db.Column(db.String)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    aliases = db.relationship('Alias', backref='individual', lazy=True, cascade='all, delete-orphan', passive_deletes=True)
    identity_documents = db.relationship('IdentityDocument', backref='individual', lazy=True, cascade='all, delete-orphan', passive_deletes=True)


    def __repr__(self):
        return f'<Individual {self.first_name} {self.second_name}>'
