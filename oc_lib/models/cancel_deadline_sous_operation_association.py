from oc_lib.db import db

cancel_deadline_sous_operation_association = db.Table(
    'cancel_deadline_sous_operation',
    db.Column('cancel_deadline_id', db.Integer, db.ForeignKey('cancel_deadline.id'), primary_key=True),
    db.Column('sous_operation_id', db.Integer, db.ForeignKey('sous_operation.id'), primary_key=True)
)
