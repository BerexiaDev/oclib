from oc_lib.db import db
from oc_lib.models import Pm

class InactifPm(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True)
    #add qualities pp models fields.

    date_debut = db.Column(db.Date)
    date_depart = db.Column(db.Date)

    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))

    __mapper_args__ = {'polymorphic_identity': 'inactif_pm'}