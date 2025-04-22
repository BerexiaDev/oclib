from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners, change_statut_pp_pm_listener

class Pm(db.Model, Repository):
    __tablename__ = "pm"
    id = db.Column(db.Integer, primary_key=True)
    nature_pm = db.Column(db.Integer)
    numero_autorisation = db.Column(db.String(50), nullable=True)
    localite = db.Column(db.String(50), nullable=False)
    localite_code = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    centre = db.Column(db.Integer)
    ville = db.Column(db.String(50))
    registre_commerce = db.Column(db.Integer)
    adresse = db.Column(db.String(100), nullable=False, server_default="")
    raison_sociale = db.Column(db.String(100), nullable=False)
    idce = db.Column(db.String, default="", server_default="")
    idf = db.Column(db.String, default="", server_default="")
    forme_juridique = db.Column(db.String(100))
    capital_social = db.Column(db.Numeric(
        precision=20, scale=3), nullable=True)
    statut = db.Column(db.Integer)  # 1 actif #2 inactif
    email = db.Column(db.String(50))
    telephone = db.Column(db.String(50))
    date_creation = db.Column(db.Date, nullable=True)
    date_radiation = db.Column(db.Date, nullable=True)
    pays = db.Column(db.String(50))
    id_pays = db.Column(db.String(50))
    creation_status = db.Column(db.Integer, default=0)
    # this will be the discriminator attribute
    type = db.Column(db.String(50))

    __mapper_args__ = {"polymorphic_identity": "pm", "polymorphic_on": type}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        register_event_listeners(type(self))
        change_statut_pp_pm_listener(type(self))