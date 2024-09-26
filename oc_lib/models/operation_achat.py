from oc_lib.db import db
from oc_lib.models.operation import Operation

class OperationAchat(Operation):
    id = db.Column(db.Integer, db.ForeignKey("operation.id"), primary_key=True, nullable=False)

    numero_declaration = db.Column(db.String(240))
    date_declaration = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "achat"}
