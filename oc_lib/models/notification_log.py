from oc_lib.db import db
from datetime import datetime
from oc_lib.repository import Repository

class NotificationLog(db.Model, Repository):
    __tablename__ = 'notification_logs'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean(), default=False)  # True: "read" False: "unread"
    code = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    message = db.Column(db.Text, nullable=False)
    pm_rs = db.Column(db.String(100), nullable=False)
    pm_rc = db.Column(db.Integer)
    pm_centre = db.Column(db.Integer)
    pc_designation = db.Column(db.String(50), nullable=False)
    pc_numero_agrement = db.Column(db.String(50))
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)
    date_modification = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # one to one relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))

    # pm_rs, pm_rc, pm_centre
    # pc_designation, pc_numero_agrement

    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # scd_id, esd_id, ep_id
    # poc_id 