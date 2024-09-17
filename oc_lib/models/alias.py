from oc_lib.db import db
from oc_lib.repository import Repository

class Alias(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    quality = db.Column(db.String)
    alias_name = db.Column(db.String)
    individual_id = db.Column(db.Integer, db.ForeignKey('individual.id'), nullable=False)

    def __repr__(self):
        return f'<Alias {self.alias_name} ({self.quality})>'