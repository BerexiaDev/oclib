from sqlalchemy import event
from sqlalchemy.orm import Session

from oc_lib.utils.exceptions import DateValidationError
from oc_lib.utils.strings import get_class_instance, date_now, convert_str_to_date
from datetime import datetime


# TODO: Bug front must send Date type not Datetime to avoid == bug
def register_event_listeners(cls):
    # @event.listens_for(cls, "after_insert")
    # @event.listens_for(cls, "after_update")
    # def change_poc_statut(mapper, connection, target):
    #     Poc = get_class_instance("oc_lib.models.poc", "Poc")
    #     Statut = get_class_instance("oc_lib.models.statut", "Statut")

    #     session = Session(connection)
    #     try:
    #         if isinstance(target, Statut):
    #             poc = session.query(Poc).filter_by(id=target.poc_id).first()

    #             if target.is_valid and convert_str_to_date(str(target.date_debut)) == datetime.today().date():
    #                 poc.statut_activite = target.statut_activite
    #                 poc.statut_agrement = target.statut_agrement
    #             else:
    #                 last_isvalid_statut = session.query(Statut).filter_by(poc_id=poc.id, is_valid=True).order_by(Statut.id.desc()).first()
    #                 if last_isvalid_statut:
    #                     poc.statut_activite = last_isvalid_statut.statut_activite
    #                     poc.statut_agrement = last_isvalid_statut.statut_agrement
    #             session.commit()
    #     except Exception as e:
    #         session.rollback()
    #         raise e
    #     finally:
    #         session.close()

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
        GerantPm = get_class_instance("oc_lib.models.gerant_pm", "GerantPm")
        CogerantPm = get_class_instance("oc_lib.models.co_gerant_pm", "CogerantPm")
        AssociePm = get_class_instance("oc_lib.models.associe_pm", "AssociePm")

        children_of_pp = [Gerant, Cogerant, AssociePp, Prepose, Representant, Suppleant, PocS, PocP]
        children_of_pm = [GerantPm, AssociePm, CogerantPm]

        if type(target) == Poc:
            if (
                    target.date_debut_activite
                    and target.date_fin_activite
                    and datetime.strptime(str(target.date_fin_activite), "%Y-%m-%d").date() < datetime.strptime(
                str(target.date_debut_activite), "%Y-%m-%d").date()
            ):
                raise DateValidationError(
                    "La date de fin activité doit être supérieure à la date de début d'activité."
                )
        elif type(target) in children_of_pp:
            if (
                    target.date_nomination
                    and target.date_demission
                    and datetime.strptime(str(target.date_demission), "%Y-%m-%d").date() < datetime.strptime(
                str(target.date_nomination), "%Y-%m-%d").date()
            ):
                raise DateValidationError(
                    "La date de démission doit être supérieure à la date de nomination."
                )
        elif type(target) in children_of_pm:
            if (
                    target.date_debut
                    and target.date_depart
                    and datetime.strptime(str(target.date_depart), "%Y-%m-%d").date() < datetime.strptime(
                str(target.date_debut), "%Y-%m-%d").date()
            ):
                raise DateValidationError(
                    "La date de depart doit être supérieure à la date de debut."
                )
        elif (
                type(target) == DeclarationFiscal
        ):
            if (
                    target.date_debut
                    and target.date_fin
                    and datetime.strptime(str(target.date_fin), "%Y-%m-%d").date() < datetime.strptime(
                str(target.date_debut), "%Y-%m-%d").date()
            ):
                raise DateValidationError(
                    "La date de fin doit être supérieure à la date de début."
                )

    return cls


def change_statut_pp_pm_listener(cls):
    @event.listens_for(cls, "before_insert")
    @event.listens_for(cls, "before_update")
    def change_pp_statut(mapper, connection, target):
        Gerant = get_class_instance("oc_lib.models.gerant", "Gerant")
        Cogerant = get_class_instance("oc_lib.models.co_gerant", "Cogerant")
        AssociePp = get_class_instance("oc_lib.models.associe_pp", "AssociePp")
        Prepose = get_class_instance("oc_lib.models.prepose", "Prepose")
        Representant = get_class_instance("oc_lib.models.representant", "Representant")
        Suppleant = get_class_instance("oc_lib.models.suppleant", "Suppleant")
        PocS = get_class_instance("oc_lib.models.poc_s", "PocS")
        PocP = get_class_instance("oc_lib.models.poc_p", "PocP")

        children_of_pp = [Gerant, Cogerant, AssociePp, Prepose, Representant, Suppleant, PocS, PocP]

        try:
            if type(target) in children_of_pp:
                if target.date_demission and target.creation_status == 1:
                    target.statut = False
                elif not target.date_demission and target.creation_status == 1:
                    target.statut = True
                else:
                    target.statut = None
        except Exception as e:
            raise e

    @event.listens_for(cls, "before_insert")
    @event.listens_for(cls, "before_update")
    def change_pm_statut(mapper, connection, target):

        GerantPm = get_class_instance("oc_lib.models.gerant_pm", "GerantPm")
        CogerantPm = get_class_instance("oc_lib.models.co_gerant_pm", "CogerantPm")
        AssociePm = get_class_instance("oc_lib.models.associe_pm", "AssociePm")
        children_of_pm = [GerantPm, AssociePm, CogerantPm]

        try:
            if type(target) in children_of_pm:
                if target.date_depart and target.creation_status == 1:
                    target.is_actif = False
                elif not target.date_depart and target.creation_status == 1:
                    target.is_actif = True
                else:
                    target.is_actif = None
        except Exception as e:
            raise e

    return cls

## MOD Add event to change PM status:
# CASE 2: Gerant PM, CO Gerant PM, Associe PM
# if date debut kayna and date depart kayne and depart >= debut => set statut 2
