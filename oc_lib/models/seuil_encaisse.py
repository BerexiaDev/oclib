from oc_lib.repository import Repository
from oc_lib.db import db
from oc_lib.utils.strings import current_year


class SeuilEncaisse(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    annee =db.Column(db.String(4), nullable=False, default=current_year()) 
    categorie_op = db.Column(db.Integer, nullable=False) # catégorie du point de change ?
    encaisse = db.Column(db.Float, nullable=False, default = 0)
    latence_jours = db.Column(db.Integer, nullable=False)
    latence_heure = db.Column(db.Integer, nullable=False) 

    lieu_implantation_id = db.Column(db.Integer, db.ForeignKey("lieu_implantation.id"))
    lieu_implantation = db.relationship("LieuImplantation")