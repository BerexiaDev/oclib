from oc_lib.repository import Repository
from oc_lib.db import db


class Currency(db.Model, Repository):
    __tablename__ = 'currency'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100))
    code = db.Column(db.Integer)
