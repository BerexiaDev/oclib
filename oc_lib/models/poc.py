from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.events_decorator import register_event_listeners
from oc_lib.models.derogation_operation_poc_association import derogation_operation_poc_association
from oc_lib.models.derogation_encaisse_poc_association import derogation_encaisse_poc_association


@register_event_listeners
class Poc(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    forme_juridique = db.Column(db.String(50), nullable=True)
    is_link = db.Column(db.Boolean, nullable=False)
    is_source = db.Column(db.Boolean, default=False)
    motif = db.Column(db.String(100))
    secteur_activite = db.Column(db.Integer)
    nature = db.Column(db.Integer)
    nom_agence = db.Column(db.String(50))
    adresse = db.Column(db.String(50), nullable=False)
    date_modification_adresse = db.Column(db.Date)
    localite = db.Column(db.String(50), nullable=False)
    localite_code = db.Column(db.String(50), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    is_agrement = db.Column(db.Boolean, nullable=False)
    is_permanent = db.Column(db.Boolean, nullable=False)
    numero_agrement = db.Column(db.String(50))
    encaisse = db.Column(db.Float, nullable=False, default=0)
    seuil_encaisse = db.Column(db.Float)
    seuil_encaisse_depasse = db.Column(db.Boolean, default=False)  # Indicates if seuil_encaisse is exceeded
    date_depassement_seuil = db.Column(db.DateTime)
    flag_retablissement_agrement = db.Column(db.Boolean)
    date_retablissement_agrement = db.Column(db.Date)
    date_modification_encaisse = db.Column(db.Date)
    date_debut_activite = db.Column(db.Date, nullable=False)
    date_fin_activite = db.Column(db.Date)
    statut_activite = db.Column(db.Integer)
    statut_agrement = db.Column(db.Integer)
    raison_sociale_pm = db.Column(db.String(100), nullable=False)

    creation_status = db.Column(db.Integer, default=0)
    categorie = db.Column(db.Integer)

    statuts = db.relationship("Statut", backref="poc", lazy=True)
    motifs = db.relationship("Motif", backref="poc", lazy=True)

    preposes = db.relationship("Prepose", backref="poc", lazy=True, cascade="all, delete")

    declarations = db.relationship("DeclarationPoc", backref="poc", lazy=True)
    declarations_ana = db.relationship("DeclarationAna", backref="mandataire")

    # One to one
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id"))

    lieu_implantation_id = db.Column(db.Integer, db.ForeignKey("lieu_implantation.id"))
    lieu_implantation = db.relationship("LieuImplantation", backref="lieu_implantation")

    #many to many
    derogation_operations = db.relationship(
        "DerogationOperation",
        secondary = derogation_operation_poc_association,
        back_populates="pocs"
    )

    derogation_encaisses = db.relationship(
        "DerogationEncaisse",
        secondary=derogation_encaisse_poc_association,
        back_populates="pocs"
    )

    # Self-referential one-to-one relationship
    linked_poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"), nullable=True)
    linked_poc = db.relationship("Poc", remote_side=[id], uselist=False)

    caisse_devises = db.relationship("CaisseDevise", cascade="all, delete")
