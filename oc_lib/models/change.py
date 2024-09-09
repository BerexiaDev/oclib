from oc_lib.db import db
from oc_lib.repository import Repository
from sqlalchemy.dialects.postgresql import JSONB

class Change(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)
    demande_id = db.Column(db.Integer, db.ForeignKey('demande.id'))