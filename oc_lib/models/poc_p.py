from oc_lib.db import db
from oc_lib.models.pp import Pp


class PocP(Pp):
    __tablename__ = 'pocp'
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    # One to one
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))

    __mapper_args__ = {"polymorphic_identity": "poc_p"}
