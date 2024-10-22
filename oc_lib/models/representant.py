from oc_lib.models.pp import Pp
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_listener


#TODO: all qualities need date debut + fin RG
@register_event_listeners
@change_statut_pp_listener
class Representant(Pp):
    id = db.Column(db.Integer, db.ForeignKey("pp.id"), primary_key=True)
    fonction = db.Column(db.Integer)
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))

    scd_inactifs_representant = db.Column(db.Integer, db.ForeignKey('scd.id'))

    # One to one
    suppleant = db.relationship(
        "Suppleant",
        backref="representant",
        uselist=False,
        foreign_keys="[Suppleant.representant_id]",
    )

    __mapper_args__ = {"polymorphic_identity": "representant"}
