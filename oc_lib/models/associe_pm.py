from sqlalchemy import Numeric
from oc_lib.db import db
from oc_lib.models.pm import Pm
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener

@register_event_listeners
@change_statut_pp_pm_listener
class AssociePm(Pm):
    id = db.Column(db.Integer, db.ForeignKey('pm.id'), primary_key=True)
    part_capital = db.Column(Numeric(precision=12, scale=2))
    date_debut = db.Column(db.Date)
    date_depart = db.Column(db.Date)
    is_actif = db.Column(db.Boolean)

    # many to one
    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))

    # one to many
    associepps = db.relationship('AssociePp', backref='AssociePm')

    # one to many
    associes = db.relationship('AssociePm', backref='AssociePm', lazy=True, foreign_keys="[AssociePm.associes_id]", remote_side=id)
    associes_id = db.Column(db.Integer, db.ForeignKey('associe_pm.id'))
    #if you do AssociePm above, you get this error 
    #sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'associe_pm.associepm_id' 
    # could not find table 'AssociePm' with which to generate a foreign key to target column 'id'

    __mapper_args__ = {'polymorphic_identity': 'associe_pm'}
