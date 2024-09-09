from oc_lib.db import db


derogation_operation_poc_association = db.Table(
    'derogation_operation_poc',
    db.Column('derogation_operation_id', db.Integer, db.ForeignKey('derogation_operation.id'), primary_key=True),
    db.Column('poc_id', db.Integer, db.ForeignKey('poc.id'), primary_key=True)
)
