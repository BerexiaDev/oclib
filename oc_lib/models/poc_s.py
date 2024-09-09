from oc_lib.db import db
from app.db.pp import Pp


class PocS(Pp):
    __tablename__ = 'pocs'
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    # One to one
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))

    __mapper_args__ = {"polymorphic_identity": "poc_s"}
