from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime


class PaimentModes(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, server_default=db.text("GENERATED ALWAYS AS IDENTITY"))
    label = db.Column(db.String)
    status = db.Column(db.Boolean, default=True)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)