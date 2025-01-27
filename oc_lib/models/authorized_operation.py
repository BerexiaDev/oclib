from oc_lib.repository import Repository
from oc_lib.db import db


class AuthorizedOperation(db.Model, Repository):
    """ Model pour les operations autorisées """

    id = db.Column(db.Integer, primary_key=True)
    # catégorie du point de change
    categorie_pc = db.Column(db.Integer, nullable=False)
    type_operation = db.Column(db.Integer, nullable=False)
    statut = db.Column(db.Boolean, default=True)
    date_activation = db.Column(db.Date, nullable=True)
    date_desactivation = db.Column(db.Date, nullable=True)
    lieu_implantations_hash = db.Column(
        db.String(50), nullable=False, default="")

    # M Pas fiable maybe load the sous operation
    sous_operation_id = db.Column(
        db.Integer, db.ForeignKey('sous_operation.id'))
    sous_operation = db.relationship("SousOperation")

    lieu_implantations = db.relationship(
        "LieuImplantation", secondary="authorized_operation_lieu_implantation", backref="authorized_operations")

    derogations = db.relationship(
        "DerogationOperation", backref="operation", lazy=True)

    solde = db.Column(db.Integer, nullable=False)
