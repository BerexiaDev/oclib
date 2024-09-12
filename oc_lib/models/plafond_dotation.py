from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import current_year


class PlafondDotation(db.Model, Repository):
    """ Model pour paramétrage plafond dotation des sous operation """
    id = db.Column(db.Integer, primary_key=True)
    annee= db.Column(db.String(4), nullable=False, default=current_year())
    plafond = db.Column(db.Float, nullable =False, default=0) # en MAD

    #many to one
    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")