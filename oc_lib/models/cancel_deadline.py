from oc_lib.repository import Repository
from oc_lib.db import db

class CancelDeadline(db.Model, Repository):
    """ Model pour délai d'annulation """

    id = db.Column(db.Integer, primary_key=True)
    categorie_pc = db.Column(db.Integer, nullable=False) # categorie du point de change
    type_operation = db.Column(db.Integer, nullable=False)
    delai = db.Column(db.Integer, nullable=False) # en minute
    statut = db.Column(db.Boolean)

        # many to one
    sous_operation_id = db.Column( 
        db.Integer, db.ForeignKey('sous_operation.id'), nullable=False)