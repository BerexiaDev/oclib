from oc_lib.db import db
from oc_lib.models.pm import Pm
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener

@register_event_listeners
@change_statut_pp_pm_listener
class CogerantPm(Pm):
    id = db.Column(db.Integer, db.ForeignKey("pm.id"), primary_key=True)
    date_debut = db.Column(db.Date)
    date_depart = db.Column(db.Date)
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    __mapper_args__ = {"polymorphic_identity": "cogerantpm"}