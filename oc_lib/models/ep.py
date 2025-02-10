from oc_lib.db import db
from oc_lib.models.pm import Pm


class Ep(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)

    apa_actif = db.Column(db.Integer, default=0)
    apna_actif = db.Column(db.Integer, default=0)
    m_actif = db.Column(db.Integer, default=0)
    m_inactif = db.Column(db.Integer, default=0)
    ama_actif = db.Column(db.Integer, default=0)
    amna_actif = db.Column(db.Integer, default=0)
    ap_inactif = db.Column(db.Integer, default=0)
    ap_total = db.Column(db.Integer, default=0)
    am_inactif = db.Column(db.Integer, default=0)
    am_total = db.Column(db.Integer, default=0)

    sequence_number = db.Column(db.Integer)

    # One to many
    mandataires = db.relationship(
        "Mandataire", backref="ep", foreign_keys="[Mandataire.ep_id]", cascade="all, delete"
    )

    declarations_ana = db.relationship("DeclarationAna", backref="ep")
    poc_ss = db.relationship("PocS", backref="ep", foreign_keys="[PocS.ep_id]", cascade="all, delete")
    pocs = db.relationship("Poc", backref="ep", foreign_keys="[Poc.ep_id]", cascade="all, delete")

    poc_ps = db.relationship("PocP", backref="ep", uselist=True)
    poc_p = db.relationship(
        "PocP",
        primaryjoin="and_(PocP.ep_id==Ep.id, or_(PocP.statut==True, PocP.statut.is_(None)))", 
        uselist=False, 
    )


    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {"polymorphic_identity": "ep"}
