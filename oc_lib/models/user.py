from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import datetime

class User(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    keycloak_id = db.Column(db.String(40))
    firstName = db.Column(db.String(120), nullable=False)
    lastName = db.Column(db.String(120), nullable=False)
    fullname = db.Column(db.String(240), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(80), nullable=False)
    type_pm = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)