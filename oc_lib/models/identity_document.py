from oc_lib.db import db
from oc_lib.repository import Repository

class IdentityDocument(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    type_of_document = db.Column(db.String)
    number = db.Column(db.String)
    individual_id = db.Column(db.Integer, db.ForeignKey('individual.id'), nullable=False)

    def __repr__(self):
        return f'<Identity Document {self.type_of_document}: {self.number}>'