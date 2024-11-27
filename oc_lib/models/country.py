from oc_lib.repository import Repository
from oc_lib.db import db


class Country(db.Model, Repository):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(2))
