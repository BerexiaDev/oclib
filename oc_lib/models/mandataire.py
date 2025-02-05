from oc_lib.db import db
from oc_lib.models.pm import Pm


class Mandataire(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)
    groupe = db.Column(db.Integer, nullable=True)
    motif = db.Column(db.Integer, nullable=True)

    ama_actif = db.Column(db.Integer, default=0)
    amna_actif = db.Column(db.Integer, default=0)

    sequence_number = db.Column(db.Integer)
    date_debut_mandat = db.Column(db.Date, nullable=False)
    date_rupture_mandat = db.Column(db.Date, nullable=True)

    # One to many
    pocs = db.relationship(
        "Poc", backref="mandataire", foreign_keys="[Poc.mandataire_id]", cascade="all, delete"
    )
    declarations_ana = db.relationship("DeclarationAna", backref="mandataire")

    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    
    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)

    __mapper_args__ = {"polymorphic_identity": "mandataire"}
