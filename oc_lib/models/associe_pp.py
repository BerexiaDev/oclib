from oc_lib.db import db
from app.db.pp import Pp


class AssociePp(Pp):
    id = db.Column(db.Integer, db.ForeignKey('pp.id'), primary_key=True)
    part_capital = db.Column(db.Integer)

    # many to one
    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    associepm_id = db.Column(db.Integer, db.ForeignKey('associe_pm.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))

    __mapper_args__ = {'polymorphic_identity': 'associe_pp'}
