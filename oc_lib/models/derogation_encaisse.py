from oc_lib.models.derogation import Derogation
from oc_lib.db import db
from oc_lib.models.derogation_encaisse_poc_association import derogation_encaisse_poc_association



class DerogationEncaisse(Derogation):
    id = db.Column(db.Integer, db.ForeignKey("derogation.id"), primary_key=True, nullable=False)
    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    scd = db.relationship("Scd", backref = "derogation_encaisse")

    encaisse = db.Column(db.Float, nullable=False, default = 0 )
    
    # Add a one-to-one relationship with Poc
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))
    poc = db.relationship("Poc", backref="derogation_encaisse")

    __mapper_args__ = {"polymorphic_identity": "derogation_encaisse"}
