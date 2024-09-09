from oc_lib.db import db
from app.db.pm import Pm


class Mandataire(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)
    groupe = db.Column(db.Integer, nullable=True)
    motif = db.Column(db.Integer, nullable=True)

    ama_actif = db.Column(db.Integer, default=0)
    amna_actif = db.Column(db.Integer, default=0)

    creation_status = db.Column(db.Integer, default=0)
    sequence_number = db.Column(db.Integer)

    # One to many
    pocs = db.relationship(
        "Poc", backref="mandataire", foreign_keys="[Poc.mandataire_id]"
    )
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    
    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "mandataire"}
