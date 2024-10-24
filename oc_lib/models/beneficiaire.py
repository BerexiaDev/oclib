from oc_lib.db import db
from oc_lib.repository import Repository


class Beneficiaire(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qualite = db.Column(db.Integer, nullable=False)
    nationalite = db.Column( db.String(120))

    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))
    numero_agrement = db.Column(db.String(50)) # of the poc that did the changes
    nom_agence = db.Column(db.String(50)) # of the poc that did the changes
    date_deactivation = db.Column(db.DateTime) # date of deactivation
    statut = db.Column(db.Boolean, default=True, nullable=False)  # True active, False inactive

    # this will be the discriminator attribute
    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "beneficiaire", "polymorphic_on": type}
