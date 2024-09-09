from oc_lib.repository import Repository
from oc_lib.db import db


class Banque(db.Model, Repository):
  __tablename__ = 'banque'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  libelle = db.Column(db.String(100))
  abreviation = db.Column(db.String(100))
  code_ancien = db.Column(db.String(10)) 
  code_bank = db.Column(db.Integer)
  en_activite = db.Column(db.Boolean)
  code_bam = db.Column(db.String(50))
  
  guichets = db.relationship('Guichet', backref='banque', lazy=True)