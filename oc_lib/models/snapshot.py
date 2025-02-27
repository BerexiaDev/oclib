from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class SnapShot(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    demande_id = db.Column(db.Integer, db.ForeignKey('demande.id'))
    snapshot_data = db.Column(JSONB)