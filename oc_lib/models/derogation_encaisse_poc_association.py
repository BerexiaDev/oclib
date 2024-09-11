from oc_lib.db import db


derogation_encaisse_poc_association = db.Table(
    'derogation_encaisse_poc',
    db.Column('derogation_encaisse_id', db.Integer, db.ForeignKey('derogation_encaisse.id'), primary_key=True),
    db.Column('poc_id', db.Integer, db.ForeignKey('poc.id'), primary_key=True)
)
