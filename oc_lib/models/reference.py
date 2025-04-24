from oc_lib.repository import Repository
from oc_lib.db import db


class Reference(db.Model, Repository):
  __tablename__ = 'reference'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  centre = db.Column(db.Integer, nullable=False)
  ville = db.Column(db.String(50), nullable=False)
  rc = db.Column(db.Integer)
  raison_sociale = db.Column(db.String(1000))
  address = db.Column(db.String(200))
  forme_juridique = db.Column(db.String(100))
  capital_social = db.Column(db.Numeric(precision=20, scale=3))
  date_creation = db.Column(db.Date, nullable=False)
  date_radiation = db.Column(db.Date, nullable=True)