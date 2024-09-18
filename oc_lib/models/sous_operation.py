from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import date_now
from oc_lib.models.cancel_deadline_sous_operation_association import cancel_deadline_sous_operation_association



class SousOperation(db.Model, Repository):
    """ Model pour paramétrage des sous opérations """

    id = db.Column(db.Integer, primary_key=True)
    type_operation = db.Column(db.Integer, nullable=False)
    code = db.Column(db.Integer, nullable=False) 
    label = db.Column(db.String, nullable=False)
    statut = db.Column(db.Boolean,nullable=False, default=True)
    date_activation=db.Column(db.Date, nullable=False, default = date_now())
    date_desactivation=db.Column(db.Date, nullable=True)
    nature_beneficiaire = db.Column(db.ARRAY(db.Integer), nullable=False, default=[])
    beneficaire_final_required = db.Column(db.Boolean, nullable=False, default=False)
    attachements = db.Column(db.ARRAY(db.String), nullable=False, default=[])

    # Many to Many
    cancel_deadlines = db.relationship('CancelDeadline', secondary=cancel_deadline_sous_operation_association, backref='sous_operations')
