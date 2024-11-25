from oc_lib.repository import Repository
from oc_lib.db import db


class AffiliationGroup(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)
    type_operator = db.Column(db.Integer, default=1)

    scds = db.relationship("Scd", backref="affiliation_group", lazy=True)
    esds = db.relationship("Esd", backref="affiliation_group", lazy=True)
    eps = db.relationship("Ep", backref="affiliation_group", lazy=True)
    mandataires = db.relationship("Mandataire", backref="affiliation_group", lazy=True)
