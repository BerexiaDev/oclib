from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy.dialects.postgresql import JSONB

class DemandeChangeModifView(db.Model):
    __tablename__ = 'demande_change_modif_view'

    id = db.Column(db.Integer, primary_key=True)
    demande_id = db.Column(db.Integer)
    demande_initiateur = db.Column(db.Integer)
    demande_date_creation = db.Column(db.Date)
    demande_scd = db.Column(db.Integer)
    demande_ep = db.Column(db.Integer)
    demande_esd = db.Column(db.Integer)
    demande_mandataire_id = db.Column(db.Integer)
    demande_poc_id = db.Column(db.Integer)
    modification_object = db.Column(db.Integer)
    modification_motif = db.Column(db.String)
    key = db.Column(db.String)
    value = db.Column(JSONB)
    oldvalue = db.Column(JSONB)