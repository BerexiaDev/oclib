from oc_lib.db import db
from oc_lib.repository import Repository


class Beneficiaire(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qualite = db.Column(db.Integer, nullable=False)
    nationalite = db.Column( db.String(120))
    date_solde = db.Column(db.Date, nullable=True) #To be removed when we handle solde properly
    solde_disponible = db.Column(db.Float, nullable=False, default=0)

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    numero_agrement = db.Column(db.String(50))
    nom_agence = db.Column(db.String(50))
    date_deactivation = db.Column(db.DateTime)
    statut = db.Column(db.Boolean, default=True, nullable=False)  # True active, False inactive

    # this will be the discriminator attribute
    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "beneficiaire", "polymorphic_on": type}
