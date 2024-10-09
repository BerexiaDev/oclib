from oc_lib.db import db
from oc_lib.models.pm import Pm


class Esd(Pm):
    id = db.Column(db.Integer, db.ForeignKey('pm.id'), primary_key=True)
    part_total = db.Column(db.Integer, default=0)  # Set default value to 0
    creation_status = db.Column(db.Integer, default=0)
    sequence_number = db.Column(db.Integer)
    groupe = db.Column(db.Integer, nullable=True)
    motif = db.Column(db.Integer, nullable=True)

    poc = db.relationship('Poc', backref='esd', uselist=False)
    
    gerant_pp = db.relationship(
        "Gerant",
        backref="esd_gerant_pp_ref",
        uselist=False,
        foreign_keys="[Gerant.esd_id]" 
    )
    gerant_pm = db.relationship('GerantPm', backref='esd', uselist=False, foreign_keys="[GerantPm.esd_id]")
    
    associe_pps = db.relationship('AssociePp', backref='esd')
    associe_pms = db.relationship('AssociePm', backref='esd', foreign_keys="[AssociePm.esd_id]")
    co_gerants = db.relationship('Cogerant', backref='esd')
    co_gerants_pms = db.relationship('CogerantPm', backref='esd', foreign_keys="[CogerantPm.esd_id]")
    inactif_gerants = db.relationship(
        "Gerant",
        backref="esd",
        uselist=True,
        foreign_keys="[Gerant.esd_inactifs_gerant]"
    )

    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)
    
    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {'polymorphic_identity': 'esd'}