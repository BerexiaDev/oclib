from oc_lib.repository import Repository
from oc_lib.db import db


class Guichet(db.Model, Repository):
    __tablename__ = "guichet"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    libelle = db.Column(db.String(100))
    adresse = db.Column(db.String(200))
    code_agency = db.Column(db.Integer, nullable=True)
    code_bank = db.Column(db.Integer)
    code_centre = db.Column(db.String(10))
    is_closed = db.Column(db.Boolean)
    code_localite = db.Column(db.String(10))
    code_bam = db.Column(db.String(10))

    banque_id = db.Column(db.Integer, db.ForeignKey("banque.id"), nullable=False)
