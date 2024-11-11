from oc_lib.db import db
from oc_lib.repository import Repository


class BackupJob(db.Model, Repository):
    __tablename__ = "backup_jobs"
    
    id = db.Column(db.Integer, primary_key=True)
    backup_time = db.Column(db.DateTime, nullable=False)
    job_id = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)