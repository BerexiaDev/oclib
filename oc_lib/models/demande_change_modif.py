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
    demande_decision = db.Column(db.Integer)
    modification_category_op = db.Column(db.Integer)
    modification_motif = db.Column(db.String)
    change_ecran = db.Column(db.String)
    change_key = db.Column(db.String)
    change_value = db.Column(JSONB)
    change_oldvalue = db.Column(JSONB)
    change_field_name = db.Column(db.String)
    change_field_value = db.Column(JSONB)
