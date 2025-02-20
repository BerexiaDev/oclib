from oc_lib.db import db
from oc_lib.repository import Repository
from oc_lib.utils.strings import date_now


class AutorisationParticuliere(db.Model, Repository):
    __tablename__ = "autorisation_particuliere"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))

    montant_supplementaire = db.Column(db.Float, nullable=False, default=0)
    numero_autorisation = db.Column(db.String(50), nullable=False)
    date_autorisation = db.Column(db.Date, nullable=False)
    statut = db.Column(db.Integer, default=1)  # 1 Encours, 2 valide
    created_by = db.Column(db.String(240), nullable=False, default='')
    date_creation = db.Column(db.Date, nullable=False, default=date_now())
    validated_by = db.Column(db.String(240))
    date_validation = db.Column(db.Date)
    date_annulation = db.Column(db.Date)
    commentaire = db.Column(db.String(200), nullable=True)
    solde = db.Column(db.Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'autorisation_particuliere', 'polymorphic_on': type}
