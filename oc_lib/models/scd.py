from oc_lib.db import db
from oc_lib.models.pm import Pm


class Scd(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True, nullable=False)
    groupe = db.Column(db.Integer, nullable=True)
    motif = db.Column(db.Integer, nullable=True)

    poc_total = db.Column(db.Integer, default=0)
    poc_actif = db.Column(db.Integer, default=0)
    poc_inactif = db.Column(db.Integer, default=0)
    part_total = db.Column(db.Integer, default=0)
    sequence_number = db.Column(db.Integer)

    # One to many
    associe_pps = db.relationship("AssociePp", backref="scd")
    associe_pms = db.relationship(
        "AssociePm", backref="scd", foreign_keys="[AssociePm.scd_id]"
    )
    co_gerants = db.relationship("Cogerant", backref="scd")
    pocs = db.relationship("Poc", backref="scd")
    inactif_gerants = db.relationship(
        "Gerant",
        backref="scd_inactif_gerant_pp_ref",
        uselist=True,
        foreign_keys="[Gerant.scd_inactifs_gerant]"
    )
    inactif_suppleants = db.relationship(
        "Suppleant",
        backref="scd_inactif_suppleant_pp_ref",
        uselist=True,
        foreign_keys="[Suppleant.scd_inactifs_suppleant]"
    )

    inactif_representants = db.relationship(
        "Representant",
        backref="esd_inactif_representant_pp_ref",
        uselist=True,
        foreign_keys="[Representant.scd_inactifs_representant]"
    )

    # One to one
    representant = db.relationship(
        "Representant",
        backref="scd", 
        uselist=False,
        foreign_keys="[Representant.scd_id]" 
    )
    gerant_pp = db.relationship(
        "Gerant",
        backref="scd",  
        uselist=False,
        foreign_keys="[Gerant.scd_id]" 
    )

    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)
    
    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "scd"}