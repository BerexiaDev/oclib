from oc_lib.models.derogation import Derogation
from oc_lib.db import db



class DerogationEncaisse(Derogation):
    id = db.Column(db.Integer, db.ForeignKey("derogation.id"), primary_key=True, nullable=False)
    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    scd = db.relationship("Scd", backref="derogation_encaisse")

    encaisse = db.Column(db.Float, nullable=False, default = 0 )
    
    # One to many
    pocs = db.relationship("Poc", backref="derogation_encaisses")