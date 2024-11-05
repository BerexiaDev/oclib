from oc_lib.repository import Repository
from oc_lib.db import db


class Localite(db.Model, Repository):
    __tablename__ = 'region'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    code = db.Column(db.Integer)

    region_id = db.Column(db.Integer, db.ForeignKey('region.code'))
