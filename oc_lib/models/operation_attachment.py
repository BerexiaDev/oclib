from oc_lib.db import db
from oc_lib.repository import Repository


class OperationAttachment(db.Model, Repository):
    
    id = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(240))
    nom_fichier = db.Column(db.String(500), nullable=False)
    full_path= db.Column(db.String(500), nullable =False)
    file_extension = db.Column(db.String(5), nullable=False)
    date_creation = db.Column(db.Date, default=db.func.now())

    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
    operation_cession_id = db.Column(db.Integer, db.ForeignKey('operation_cession.id'))
