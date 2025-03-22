from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy import text


class PmDocument(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"), nullable=False)
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"), nullable=False)
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"), nullable=False)
    intitule_document = db.Column(db.String(1000), nullable=False)
    nom_fichier = db.Column(db.String(1000), nullable=False)
    date_creation = db.Column(db.Date, default=db.func.now())
    full_path= db.Column(db.String(250))

    # 1. Only PDF format allowed
    file_extension = db.Column(db.String(5), nullable=False)
    file_extension_check = db.CheckConstraint(text("file_extension IN ('PDF')"))

