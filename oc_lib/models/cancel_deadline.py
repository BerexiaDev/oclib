from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.models.cancel_deadline_sous_operation_association import cancel_deadline_sous_operation_association

# A voir pour statut pour l'unicité

class CancelDeadline(db.Model, Repository):
    """ Model pour délai d'annulation """

    id = db.Column(db.Integer, primary_key=True)
    categorie_op = db.Column(db.Integer, nullable=False) # categorie du point de change
    type_operation = db.Column(db.Integer, nullable=False)
    delai = db.Column(db.Integer, nullable=False) # en minute
    
    #Many to Many
    sous_operations = db.relationship('SousOperation', secondary=cancel_deadline_sous_operation_association, backref='cancel_deadlines')