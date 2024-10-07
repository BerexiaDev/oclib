from oc_lib.db import db
from oc_lib.models import Pp

class InactifPp(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    #add qualities pp models fields.
    fonction = db.Column(db.Integer)
    representant_id = db.Column(db.Integer, db.ForeignKey("representant.id"))

    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))
    ep_id = db.Column(db.Integer, db.ForeignKey('ep.id'))

    __mapper_args__ = {'polymorphic_identity': 'inactif_pp'}