from oc_lib.db import db
from oc_lib.models.pm import Pm
from sqlalchemy import or_

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
    associe_pms = db.relationship("AssociePm", backref="scd", foreign_keys="[AssociePm.scd_id]")
    co_gerants = db.relationship("Cogerant", backref="scd")
    pocs = db.relationship("Poc", backref="scd")

    # One to many (Actif + Inactif)
    representants = db.relationship("Representant", backref="scd", uselist=True)
    representant = db.relationship(
        "Representant",
        primaryjoin="and_(Representant.scd_id==Scd.id,Representant.creation_status!=4 ,or_(Representant.statut==True, Representant.statut.is_(None)))", 
        uselist=False, 
    )

    # One to many (Actif + Inactif)
    gerants = db.relationship("Gerant", backref="scd", uselist=True)
    gerant_pp = db.relationship(
        "Gerant",
        primaryjoin="and_(Gerant.scd_id==Scd.id,Gerant.creation_status!=4 ,or_(Gerant.statut==True, Gerant.statut.is_(None)))", 
        uselist=False
    )
    
    # Many to one
    affiliation_group_id = db.Column(db.Integer, db.ForeignKey('affiliation_group.id'))
    affiliation_group_motif = db.Column(db.String(255), nullable=True)
    
    numero_decision_autorisation = db .Column(db.String(255))
    date_decision_autorisation = db.Column(db.Date)

    __mapper_args__ = {"polymorphic_identity": "scd"}
