from sqlalchemy import event
from sqlalchemy.orm import Session

from oc_lib.utils.exceptions import DateValidationError
from oc_lib.utils.strings import get_class_instance


# TODO: Bug front must send Date type not Datetime to avoid == bug
def register_event_listeners(cls):
    @event.listens_for(cls, "after_insert")
    @event.listens_for(cls, "after_update")
    def change_poc_statut(mapper, connection, target):
        Poc = get_class_instance("oc_lib.models.poc", "Poc")
        Statut = get_class_instance("oc_lib.models.statut", "Statut")
        
        session = Session(connection)
        try:
            if isinstance(target, Statut):
                poc = session.query(Poc).filter_by(id=target.poc_id).first()

                if target.is_valid:
                    poc.statut_activite = target.statut_activite
                else:
                    previous_statut = session.query(Statut).filter_by(poc_id=poc.id).order_by(Statut.id.desc()).offset(1).first()
                    if previous_statut:
                        poc.statut_activite = previous_statut.statut_activite
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @event.listens_for(cls, "before_insert")
    @event.listens_for(cls, "before_update")
    def validate_dates(mapper, connection, target):
        Poc = get_class_instance("oc_lib.models.poc", "Poc")
        DeclarationFiscal = get_class_instance("oc_lib.models.declaration_fiscal", "DeclarationFiscal")

        # Child classes of Pp
        Gerant = get_class_instance("oc_lib.models.gerant", "Gerant")
        Cogerant = get_class_instance("oc_lib.models.co_gerant", "Cogerant")
        AssociePp = get_class_instance("oc_lib.models.associe_pp", "AssociePp")
        Prepose = get_class_instance("oc_lib.models.prepose", "Prepose")
        Representant = get_class_instance("oc_lib.models.representant", "Representant")
        Suppleant = get_class_instance("oc_lib.models.suppleant", "Suppleant")
        PocS = get_class_instance("oc_lib.models.poc_s", "PocS")
        PocP = get_class_instance("oc_lib.models.poc_p", "PocP")

        children_of_pp = [Gerant, Cogerant, AssociePp, Prepose, Representant, Suppleant, PocS, PocP]

        if type(target) == Poc:
            if (
                target.date_debut_activite
                and target.date_fin_activite
                and target.date_fin_activite <= target.date_debut_activite
            ):
                raise DateValidationError(
                    "La date de fin activité doit être supérieure à la date de début d'activité."
                )
        elif type(target) in children_of_pp:
            if (
                target.date_nomination
                and target.date_demission
                and target.date_demission <= target.date_nomination
            ):
                raise DateValidationError(
                    "La date de démission doit être supérieure à la date de nomination."
                )
        elif (
            type(target) == DeclarationFiscal
        ):
            if (
                target.date_debut
                and target.date_fin
                and target.date_fin <= target.date_debut
            ):
                raise DateValidationError(
                    "La date de fin doit être supérieure à la date de début."
                )

    return cls
