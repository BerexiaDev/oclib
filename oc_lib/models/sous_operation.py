from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import date_now
from sqlalchemy.dialects.postgresql import ARRAY



class SousOperation(db.Model, Repository):
    """ Model pour paramétrage des sous opérations """

    id = db.Column(db.Integer, primary_key=True)
    type_operation = db.Column(db.Integer, nullable=False)
    # code de la sous operation A###, V###, C###
    code = db.Column(db.String(4), nullable=False, unique=True)
    code_statistique = db.Column(db.Integer)
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

    support_mad = db.Column(ARRAY(db.Integer), nullable=False)
    support_devise = db.Column(ARRAY(db.Integer), nullable=False)

    declaration_importation = db.Column(db.Boolean, default=False)

    #One to Many
    cancel_deadlines = db.relationship('CancelDeadline',backref="sous_operation", cascade="all, delete-orphan") 

    # Relationship with PlafondDotation
    plafond_dotations = db.relationship(
        "PlafondDotation", 
        back_populates="sous_operation", 
        cascade="all, delete-orphan"
    )