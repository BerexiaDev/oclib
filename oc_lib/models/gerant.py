from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_listener

@register_event_listeners
@change_statut_pp_listener
class Gerant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)

    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey('scd.id'))
    esd_id = db.Column(db.Integer, db.ForeignKey('esd.id'))
    
    scd_inactifs_gerant = db.relationship("Scd", backref="inactif_gerants")

    __mapper_args__ = {"polymorphic_identity": "gerant"}
