from oc_lib.db import db
from oc_lib.repository import Repository

class Individual(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    data_id = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String)
    second_name = db.Column(db.String)
    third_name = db.Column(db.String)
    fourth_name = db.Column(db.String)
    # Relationships
    aliases = db.relationship('Alias', backref='individual', lazy=True)
    documents = db.relationship('Document', backref='individual', lazy=True)

    def __repr__(self):
        return f'<Individual {self.first_name} {self.second_name}>'