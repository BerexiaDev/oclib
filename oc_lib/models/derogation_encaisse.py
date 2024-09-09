from oc_lib.models.derogation import Derogation
from oc_lib.db import db

# point de change simple ou bien multiple


class DerogationEncaisse(Derogation):
    id = db.Column(db.Integer, db.ForeignKey("derogation.id"), primary_key=True, nullable=False)
    encaisse = db.Column(db.Float, nullable=False, default = 0 )
    
    # One to many
    pocs = db.relationship("Poc", backref="derogationencaisse")
    
    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id"))
