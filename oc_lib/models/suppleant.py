from oc_lib.db import db
from oc_lib.models.pp import Pp
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_listener

@register_event_listeners
@change_statut_pp_listener
class Suppleant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    representant_id = db.Column(db.Integer, db.ForeignKey("representant.id"))
    representant = db.relationship("Representant", backref="suppleant_association",foreign_keys="[Representant.suppleant_id]")

    __mapper_args__ = {"polymorphic_identity": "suppleant"}