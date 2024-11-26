from sqlalchemy.orm import validates

from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener
from oc_lib.utils.validators import validate_cim, validate_normal_pattern, validate_cni


class Pp(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    nature_piece = db.Column(db.String(50))
    numero_piece = db.Column(db.String(50))
    nationalite = db.Column(db.String(50))
    adresse = db.Column(db.String(100))
    email = db.Column(db.String)
    phone = db.Column(db.String)
    nature_pp = db.Column(db.String(50))
    type = db.Column(db.String(50))
    date_nomination = db.Column(db.Date, nullable=False, default=db.func.now())     # date appointment
    date_demission = db.Column(db.Date)      # date resignation
    statut = db.Column(db.Boolean)
    creation_status = db.Column(db.Integer, default=0)

    __mapper_args__ = {'polymorphic_identity': 'pp', 'polymorphic_on': type}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        register_event_listeners(type(self))
        change_statut_pp_pm_listener(type(self))

    @validates('numero_piece')
    def validate_numero_piece_value(self, key, value):
        if self.nature_piece == "CNI" and self.nature_pp in ["MR", "MRE"]:
            return validate_cni(key, value)
        elif self.nature_piece == "CIM" and self.nature_pp == "ER":
            return validate_cim(key, value)
        elif self.nature_piece == "Passport" and self.nature_pp == "ENR":
            return validate_normal_pattern(key, value)
        
    @validates('adresse')
    def validate_adresse(self, key, adresse):
        if self.type in ["cogerant", "gerant"] and not adresse:
            raise ValueError("L'addresse est obligatoir.")
        return adresse
