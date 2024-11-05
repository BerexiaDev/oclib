from oc_lib.repository import Repository
from oc_lib.db import db


class Region(db.Model, Repository):
    __tablename__ = 'region'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    code = db.Column(db.Integer, unique=True)

    localites = db.relationship("localite", backref="region", uselist=True)
