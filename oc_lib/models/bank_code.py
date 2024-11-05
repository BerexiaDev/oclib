from oc_lib.repository import Repository
from oc_lib.db import db


class BankCode(db.Model, Repository):
    __tablename__ = 'bank_code'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    code = db.Column(db.Integer)
