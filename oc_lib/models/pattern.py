from oc_lib.db import db
from oc_lib.repository import Repository


class Pattern(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.Integer)