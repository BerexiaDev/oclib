from oc_lib.db import db
from app.db.pp import Pp


class Gerant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)

    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))

    __mapper_args__ = {"polymorphic_identity": "gerant"}
