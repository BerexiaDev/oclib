from oc_lib.db import db
from oc_lib.repository import Repository
from oc_lib.utils.constants import SupportOperationDevise

class OperationDevise(db.Model, Repository):
    __tablename__ = 'operation_devise'
    
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(100))
    montant_devise = db.Column(db.Float)
    cours = db.Column(db.Float)
    montant_mad = db.Column(db.Float)
    support = db.Column(db.Integer)
    
    operation_id = db.Column(db.Integer, db.ForeignKey('operation.id'))
    operation_cession_id = db.Column(db.Integer, db.ForeignKey('operation_cession.id'))

    @staticmethod
    def validate_wrapper(self):
        if self.operation_id:
            if not self.support:
                raise ValueError(
                    "support field is required."
                )
            elif self.support == SupportOperationDevise.BILLET_DE_BANQUE.value:
                # Validate all fields
                if not all([self.label, self.montant_devise, self.cours, self.montant_mad]):
                    raise ValueError(
                        "For BILLET_DE_BANQUE, all fields (label, montant_devise, cours, montant_mad) are required."
                    )
            else:
                # Validate support and montant_mad only
                if not self.support or not self.montant_mad:
                    raise ValueError(
                        "For other support types, 'support' and 'montant_mad' are required."
                    )
        elif self.operation_cession_id:
            if not all([self.label, self.montant_devise, self.cours, self.montant_mad]):
                raise ValueError(
                    "All fields (label, montant_devise, cours, montant_mad) are required."
                )


    def save(self, *args, **kwargs):
        try:
            self.validate_wrapper(self)
            super(OperationDevise, self).save(*args, **kwargs)
        except ValueError as e:
            print(f"Error while saving OperationDevise: {str(e)}")
            raise ValueError(e)
