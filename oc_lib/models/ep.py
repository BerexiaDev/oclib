from oc_lib.db import db
from oc_lib.models.pm import Pm


class Ep(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)

    apa_actif = db.Column(db.Integer, default=0)
    apna_actif = db.Column(db.Integer, default=0)
    m_actif = db.Column(db.Integer, default=0)
    ama_actif = db.Column(db.Integer, default=0)
    amna_actif = db.Column(db.Integer, default=0)

    sequence_number = db.Column(db.Integer)

    # One to many
    mandataires = db.relationship(
        "Mandataire", backref="ep", foreign_keys="[Mandataire.ep_id]", cascade="all, delete"
    )
    poc_ss = db.relationship("PocS", backref="ep", foreign_keys="[PocS.ep_id]", cascade="all, delete")
    pocs = db.relationship("Poc", backref="ep", foreign_keys="[Poc.ep_id]", cascade="all, delete")
    inactif_pocps = db.relationship(
        "PocP",
        backref="ep_pocp_pp_ref",
        uselist=True,
        foreign_keys="[PocP.scd_inactifs_pocp]",
        cascade="all, delete"
    )

    # One to one
    poc_p = db.relationship(
        "PocP",
        backref="ep",
        uselist=False,
        foreign_keys="[PocP.ep_id]",
        cascade="all, delete"
    )

    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)

    numero_decision_autorisation = db.Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "ep"}
