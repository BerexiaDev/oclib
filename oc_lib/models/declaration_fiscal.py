from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners


@register_event_listeners
class DeclarationFiscal(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.String(240), nullable=False, server_default="")

    # Fiscal declaration details
    denomination_pm = db.Column(db.String(100), nullable=False)
    centre_pm = db.Column(db.Integer, nullable=False)
    rc_pm = db.Column(db.Integer, nullable=False)
    date_declaration = db.Column(db.Date, default=db.func.now())
    annee_comptable_de = db.Column(db.Integer, nullable=False)
    date_debut = db.Column(db.Date, nullable=False, default=db.func.now())
    date_fin = db.Column(db.Date, nullable=False,default=db.func.now())

    # Formulaire fields
    capital_social = db.Column(db.Float, nullable=False)
    capitaux_propres = db.Column(db.Float, nullable=False)
    chiffre_affaires = db.Column(db.Float, nullable=False)
    resultat_exploitation = db.Column(db.Float, nullable=False)
    resultat_net = db.Column(db.Float, nullable=False)
    resultat_fiscal = db.Column(db.Float, nullable=False)
    resultat_financier = db.Column(db.Float, nullable=False)
    charges_personnel = db.Column(db.Float, nullable=False)
    charges_exploitation = db.Column(db.Float, nullable=False)
    produits_financiers = db.Column(db.Float, nullable=False)
    documents = db.relationship('DeclarationDocs', backref='declarationfiscal', lazy='dynamic')
    
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))