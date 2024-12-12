from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import date_now


class SousOperation(db.Model, Repository):
    """ Model pour paramétrage des sous opérations """

    id = db.Column(db.Integer, primary_key=True)
    type_operation = db.Column(db.Integer, nullable=False)
    # code de la sous operation A###, V###, C###
    code = db.Column(db.String(4), nullable=False, unique=True)
    code_statistique = db.Column(db.Integer, unique=True)  # code statistique
    label = db.Column(db.String, nullable=False)
    statut = db.Column(db.Boolean, nullable=False, default=True)
    date_activation = db.Column(db.Date, nullable=False, default=date_now())
    date_desactivation = db.Column(db.Date, nullable=True)
    nature_beneficiaire = db.Column(
        db.ARRAY(db.Integer), nullable=False, default=[])
    nature_beneficiaire_final = db.Column(
        db.ARRAY(db.Integer), nullable=False, default=[])
    beneficiaire_final_required = db.Column(
        db.Boolean, nullable=False, default=False)
    attachements = db.Column(db.ARRAY(db.String), nullable=False, default=[])
    declaration_importation = db.Column(db.Boolean, default=False)

    # many to one
    cancel_deadline_id = db.Column(
        db.Integer, db.ForeignKey('cancel_deadline.id'))
