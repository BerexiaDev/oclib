from oc_lib.db import db

cancel_deadline_sous_operation_association = db.Table(
    'authorized_operation_lieu_implantation',
    db.Column('authorized_operation_id', db.Integer, db.ForeignKey('authorized_operation.id'), primary_key=True),
    db.Column('lieu_implantation_id', db.Integer, db.ForeignKey('lieu_implantation.id'), primary_key=True)
)
