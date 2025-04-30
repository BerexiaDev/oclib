from oc_lib.db import db
from oc_lib.repository import Repository


class SynchronizationJob(db.Model, Repository):
    __tablename__ = "synchronization_job"
    
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)