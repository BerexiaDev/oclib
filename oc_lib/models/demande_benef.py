from oc_lib.db import db
from oc_lib.repository import Repository
from datetime import date


class DemandeBenef(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean)
    etape = db.Column(db.Integer)
    initiateur = db.Column(db.Integer)
    created_by = db.Column(db.String(240), nullable=False, server_default="")
    validateurs = db.Column(db.ARRAY(db.String(240)))
    valide_oc = db.Column(db.Boolean, default=False)
    valide_manager_oc = db.Column(db.Boolean, default=False)
    avancement = db.Column(db.Boolean, default=False)
    date_creation = db.Column(db.Date, default=date.today, onupdate=date.today)

    change = db.relationship(
        "Change", backref="demande", lazy=True, uselist=False)
