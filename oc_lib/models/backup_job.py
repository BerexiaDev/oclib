from oc_lib.db import db
from oc_lib.repository import Repository


class BackupJob(db.Model, Repository):
    __tablename__ = "backup_jobs"
    
    backup_time= None
    job_id=None
    status= None
    created_on= None