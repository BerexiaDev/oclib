from oc_lib.db import db
from oc_lib.repository import Repository



class Client(db.Model, Repository):
    id = db.Column(db.Integer,primary_key=True)
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    phone = db.Column(db.String)

    __mapper_args__ = {"polymorphic_identity": "client"}