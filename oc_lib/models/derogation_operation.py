from oc_lib.models.derogation import Derogation
from oc_lib.db import db

class DerogationOperation(Derogation):
    __tablename__ = "derogation_operation"
    id = db.Column(db.Integer, db.ForeignKey("derogation.id"), primary_key=True, nullable=False)

    # Operateurs Pm    
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    scd = db.relationship("Scd", backref="derogation_operation")

    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    esd = db.relationship("Esd", backref="derogation_operation")

    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    ep = db.relationship("Ep", backref="derogation_operation")

    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id"))
    mandataire = db.relationship("Mandataire", backref="derogation_operation")

    categorie_pc = db.Column(db.Integer, nullable =False)
    
    
    # Add a one-to-one relationship with Poc
    poc_id = db.Column(db.Integer, db.ForeignKey("poc.id"))
    poc = db.relationship("Poc", backref="derogation_operation")
    
    authorized_operation_id = db.Column(db.Integer, db.ForeignKey("authorized_operation.id"))
    
    is_included = db.Column(db.Boolean, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "derogation_operation"}







