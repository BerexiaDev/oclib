from oc_lib.repository import Repository
from oc_lib.db import db
from datetime import date
from sqlalchemy.dialects.postgresql import JSONB


class Modification(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    motif = db.Column(db.String(300), unique=True)
    modifications = db.Column(JSONB)
    op_category = db.Column(db.Integer)
    motif_status = db.Column(db.Boolean, default=True)
    is_add = db.Column(db.Boolean)
    date_activation = db.Column(db.Date, default=date.today)
    date_modification = db.Column(db.Date, default=date.today, onupdate=date.today)
    date_desactivation = db.Column(db.Date)
    demandes = db.relationship("Demande", back_populates="modification", lazy=True)
    pattern_id = db.Column(db.Integer, db.ForeignKey("pattern.id"))
    pattern = db.relationship('Pattern', back_populates='modification', lazy=True)

