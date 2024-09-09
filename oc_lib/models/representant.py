from oc_lib.models.pp import Pp
from oc_lib.db import db


#TODO: all qualities need date debut + fin RG
class Representant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))

    # One to one
    suppleant = db.relationship(
        "Suppleant",
        backref="representant",
        uselist=False,
        foreign_keys="[Suppleant.representant_id]",
    )

    __mapper_args__ = {"polymorphic_identity": "representant"}
