from oc_lib.db import db
from app.db.pp import Pp


class Prepose(Pp):
    __tablename__ = 'prepose'
    id = db.Column(db.Integer, db.ForeignKey('pp.id'), primary_key=True)
    poc_id = db.Column(db.Integer, db.ForeignKey('poc.id'))

    __mapper_args__ = {'polymorphic_identity': 'prepose'}
