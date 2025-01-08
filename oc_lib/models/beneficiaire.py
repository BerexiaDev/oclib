from oc_lib.db import db
from oc_lib.repository import Repository


class Beneficiaire(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qualite = db.Column(db.Integer, nullable=False)
    nationalite = db.Column( db.String(120))
    id_pays = db.Column( db.String(120))

    date_deactivation = db.Column(db.DateTime) # date of deactivation
    statut = db.Column(db.Boolean, default=True, nullable=False)  # True active, False inactive

    date_modification = db.Column(db.DateTime)
    modified_by = db.Column(db.String(150))
    motif_modification = db.Column(db.String(100))

    # this will be the discriminator attribute 
    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "beneficiaire", "polymorphic_on": type}
