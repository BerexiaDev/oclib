from datetime import datetime
from oc_lib.db import db
from oc_lib.repository import Repository


class AlertLog(db.Model, Repository):
    __tablename__ = 'alert_log'

    id = db.Column(db.Integer, primary_key=True)
    pc_id = db.Column(db.Integer, nullable=True)
    pc_agreement_number = db.Column(db.String(100), nullable=True)
    pc_designation = db.Column(db.String(255), nullable=True)
    triggered_by = db.Column(db.String(100), nullable=False)
    triggered_by_id = db.Column(db.Integer, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

    alert_code = db.Column(db.String(50), nullable=False)
    alert_name = db.Column(db.String(255), nullable=False)
