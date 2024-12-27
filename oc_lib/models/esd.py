from oc_lib.db import db
from oc_lib.models.pm import Pm


class Esd(Pm):
    id = db.Column(db.Integer, db.ForeignKey('pm.id'), primary_key=True)
    part_total = db.Column(db.Integer, default=0)  # Set default value to 0
    sequence_number = db.Column(db.Integer)
    groupe = db.Column(db.Integer, nullable=True)
    motif = db.Column(db.Integer, nullable=True)

    poc = db.relationship('Poc', backref='esd', uselist=False, cascade="all, delete")

    gerants_pp = db.relationship("Gerant", backref="esd", uselist=True, cascade="all, delete")
    gerant_pp = db.relationship(
        "Gerant",
        primaryjoin="and_(Gerant.esd_id==Esd.id,or_(Gerant.statut==True, Gerant.statut.is_(None)))",
        uselist=False
    )
    gerant_pms = db.relationship("GerantPm", backref="esd", uselist=True, foreign_keys="[GerantPm.esd_id]",
                                 cascade="all, delete")
    gerant_pm = db.relationship(
        "GerantPm",
        primaryjoin="and_(GerantPm.esd_id==Esd.id,or_(GerantPm.is_actif==True, GerantPm.is_actif.is_(None)))",
        uselist=False
    )

    associe_pps = db.relationship('AssociePp', backref='esd', cascade="all, delete")
    associe_pms = db.relationship('AssociePm', backref='esd', foreign_keys="[AssociePm.esd_id]", cascade="all, delete")

    co_gerants = db.relationship('Cogerant', backref='esd', cascade="all, delete")
    co_gerants_pms = db.relationship('CogerantPm', backref='esd', foreign_keys="[CogerantPm.esd_id]",
                                     cascade="all, delete")

    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)
    affiliation_group = db.relationship('AffiliationGroup', back_populates='esds', lazy=True)

    __mapper_args__ = {'polymorphic_identity': 'esd'}
