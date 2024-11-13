from oc_lib.repository import Repository
from oc_lib.db import db


class DraftReference(db.Model, Repository):
    __tablename__ = 'draft_reference'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    centre = db.Column(db.Integer, nullable=False)
    rc = db.Column(db.Integer, nullable=False)
    date_creation = db.Column(db.Date, nullable=False)
    status = db.Column(db.Integer, default=0)
    column_name = db.Column(db.String(100))
    old_value = db.Column(db.String(250))
    new_value = db.Column(db.String(250))
    motif = db.Column(db.String(250))
