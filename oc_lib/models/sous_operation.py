from oc_lib.repository import Repository
from oc_lib.db import db
from app.main.utils.strings import date_now

# add nature_beneficiaire ARRAY(db.Integer) multiple choice (page 11)

class SousOperation(db.Model, Repository):
    """ Model pour paramétrage des sous opérations """

    id = db.Column(db.Integer, primary_key=True)
    type_operation = db.Column(db.Integer, nullable=False)
    code = db.Column(db.Integer, nullable=False) 
    label = db.Column(db.String, nullable=False)
    statut = db.Column(db.Boolean,nullable=False, default=True)
    date_activation=db.Column(db.Date, nullable=False, default = date_now())
    date_desactivation=db.Column(db.Date, nullable=True)
