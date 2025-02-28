from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import current_year, date_now


class ComplementDotation(db.Model, Repository):
    """ Model pour paramétrage des complément de dotation"""

    id = db.Column(db.Integer, primary_key=True)
    annee = db.Column(db.String(4), nullable=False, default=current_year())
    label = db.Column(db.String(100), nullable=False, default="")
    nature_beneficiaire = db.Column(db.ARRAY(db.Integer), nullable=False, default=[])
    base_calcul = db.Column(db.String(100), nullable=False, default="")
    percentage = db.Column(db.Float, nullable=False, default = 0 )
    plafond= db.Column(db.Float, nullable=False, default = 0)
    statut = db.Column(db.Boolean)
    creation_date = db.Column(db.Date, nullable=False, default=date_now())

    sous_operation_id = db.Column(db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")
    