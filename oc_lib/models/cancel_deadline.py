from oc_lib.repository import Repository
from oc_lib.db import db

# A voir pour statut pour l'unicité

class CancelDeadline(db.Model, Repository):
    """ Model pour délai d'annulation """

    id = db.Column(db.Integer, primary_key=True)
    categorie_op = db.Column(db.Integer, nullable=False)
    type_operation = db.Column(db.Integer, nullable=False)
    delai = db.Column(db.Integer, nullable=False) # en minute
    statut= db.Column(db.Boolean, nullable=False)
    
    sous_operations = db.relationship('SousOperation', secondary='cancel_deadline_sous_operation', backref='cancel_deadlines')