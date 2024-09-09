from oc_lib.db import db
from app.db.pm import Pm

class Ep(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)

    apa_actif = db.Column(db.Integer, default=0)
    apna_actif = db.Column(db.Integer, default=0)
    m_actif = db.Column(db.Integer, default=0)
    ama_actif = db.Column(db.Integer, default=0)
    amna_actif = db.Column(db.Integer, default=0)

    creation_status = db.Column(db.Integer, default=0)
    sequence_number = db.Column(db.Integer)

    # One to many
    mandataires = db.relationship(
        "Mandataire", backref="ep", foreign_keys="[Mandataire.ep_id]"
    )
    poc_ss = db.relationship("PocS", backref="ep", foreign_keys="[PocS.ep_id]")
    pocs = db.relationship("Poc", backref="ep", foreign_keys="[Poc.ep_id]")

    # One to one
    poc_p = db.relationship("PocP", backref="ep", uselist=False)

    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))

    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "ep"}
