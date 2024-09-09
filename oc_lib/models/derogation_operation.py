from app.db.derogation import Derogation
from oc_lib.db import db
from app.db.derogation_poc_association import derogation_operation_poc_association


class DerogationOperation(Derogation):
    id = db.Column(db.Integer, db.ForeignKey("derogation.id"), primary_key=True, nullable=False)

    # Operateurs PM    
    scd_id = db.Column(db.Integer, db.ForeignKey("scd.id"))
    esd_id = db.Column(db.Integer, db.ForeignKey("esd.id"))
    ep_id = db.Column(db.Integer, db.ForeignKey("ep.id"))
    mandataire_id = db.Column(db.Integer, db.ForeignKey("mandataire.id"))

    categorie_pc =db.Column(db.Integer, nullable =False)
    
    # Many to many
    pocs = db.relationship("Poc",secondary=derogation_operation_poc_association,back_populates="derogation_operations")
    authorized_operation_id = db.Column(db.Integer, db.ForeignKey("authorized_operation.id"))
    
    is_included = db.Column(db.Boolean, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "derogation_operation"}

    


    

    
