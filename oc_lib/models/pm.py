from oc_lib.repository import Repository
from oc_lib.db import db


class Pm(db.Model, Repository):
    __tablename__ = "pm"
    id = db.Column(db.Integer, primary_key=True)
    nature_pm = db.Column(db.Integer)
    numero_autorisation = db.Column(db.String(50), nullable=True)
    localite = db.Column(db.String(50), nullable=False)
    localite_code = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    centre = db.Column(db.Integer)
    ville = db.Column(db.String(50))
    registre_commerce = db.Column(db.Integer)
    adresse = db.Column(db.String(100))
    raison_sociale = db.Column(db.String(100), nullable=False)
    idce = db.Column(db.String(50))
    idf = db.Column(db.String(100))
    forme_juridique = db.Column(db.String(100))
    capital_social = db.Column(db.Numeric(precision=20, scale=3))
    statut = db.Column(db.Integer)
    email = db.Column(db.String(50))
    telephone = db.Column(db.String(50))
    date_creation = db.Column(db.Date, nullable=True)
    date_radiation = db.Column(db.Date, nullable=True)
    pays = db.Column(db.String(50))
    id_pays = db.Column(db.String(50))

    # this will be the discriminator attribute
    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "pm", "polymorphic_on": type}
