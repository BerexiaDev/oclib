from oc_lib.db import db
from app.db.pp import Pp


class Suppleant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    representant_id = db.Column(db.Integer, db.ForeignKey("representant.id"))

    __mapper_args__ = {"polymorphic_identity": "suppleant"}