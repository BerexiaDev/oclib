from sqlalchemy import asc, desc

from oc_lib.models.user import User
from oc_lib.utils.constants import QUALITE_BENEFICIAIRE_MAPPING, PAYMENT_METHODS_MAPPING, OPERATORS_WITH_TYPE

# autorisation_particuliere_pm
def get_beneficiaire_pm_qualite(item, _):
    if getattr(item, "beneficiaire_pm", None):
        return QUALITE_BENEFICIAIRE_MAPPING.get(item.beneficiaire_pm.qualite, "")
    return ""


def get_beneficiaire_pm_field_value(item, field_name):
    if getattr(item, "beneficiaire_pm", None):
        return getattr(item.beneficiaire_pm, field_name)
    return ""


# autorisation_particuliere_pp
def get_beneficiaire_pp_qualite(item, _):
    if getattr(item, "beneficiaire_pp", None):
        return QUALITE_BENEFICIAIRE_MAPPING.get(item.beneficiaire_pp.qualite, "")
    return ""

def get_beneficiaire_pp_field_value(item, field_name):
    if getattr(item, "beneficiaire_pp", None):
        return getattr(item.beneficiaire_pp, field_name)

    return ""


# user
def get_users_list(args):
    query = User.query

    sort_key = args.get("sort_key", "keycloak_id")
    sort_order = args.get("sort_order")
    fullname = args.get("search_value", "")

    if fullname:
        query = query.filter(User.fullname.ilike(f"%{fullname}%"))

    query = query.order_by(
        asc(sort_key) if sort_order == 1 else desc(sort_key))

    return query.all()


# cnasnu
def get_only_date(item, field_name):
    if item.get(field_name):
        return item.get(field_name).strftime("%b %d, %Y")
    return ""


def get_cin(item, _):
    if getattr(item, "cin", None):
        return "****".join(item.cin)
    return ""


def get_passport(item, _):
    if getattr(item, "passport", None):
        return "****".join(item.passport)
    return ""


# cancel_deadline
def get_delai(item, _):
    return f"{item.delai} Minutes"


# complement dotation
def get_nature_beneficiaire(item, _):
    if getattr(item, "nature_beneficiaire", None):
        return ", ".join([QUALITE_BENEFICIAIRE_MAPPING.get(n, "") for n in getattr(item, "nature_beneficiaire", [])])
    return ""


# seuil encaisse
def get_latence_jours(item, _):
    return f"J + {item.latence_jours} à {item.latence_heure}h"


# derogration enciase
def get_operator_pm(item, _):
    if getattr(item, "scd", None):
        return f"{item.scd.registre_commerce}/{item.scd.raison_sociale}"
    return ""


def get_derogration_op(item, _):
    matching_one = next(filter(lambda operator: operator["code"] == item.categorie_pc, OPERATORS_WITH_TYPE), None)
    if matching_one and getattr(item, matching_one["type"], None):
        op = getattr(item, matching_one['type'])
        return f"{op.registre_commerce}/{op.raison_sociale}"
    return ""


# authorized operation
def get_sous_operation_code(item, _):
    if getattr(item, "sous_operation", None):
        return item.sous_operation.code
    return ""


def get_sous_operation_code_statistique(item, _):
    if getattr(item, "sous_operation", None):
        return item.sous_operation.code_statistique
    return ""


def get_sous_operation_label(item, _):
    if getattr(item, "sous_operation", None):
        return item.sous_operation.label
    return ""


def get_sous_operation_lieu_implantations(item, _):
    if getattr(item, "lieu_implantations", None):
        return ", ".join([lieu.label for lieu in item.lieu_implantations])
    return ""


def get_sous_operaton_label(item, _):
    if getattr(item, "sous_operation", None):
        return item.sous_operation.label
    return ""


def get_payment_method(item, field_name):
    if getattr(item, field_name, None):
        return ", ".join([PAYMENT_METHODS_MAPPING.get(method, "") for method in getattr(item, field_name, [])])
    return ""


# modification
def get_pattern(item, _):
    if getattr(item, "pattern", None):
        return item.pattern._type
    return ""


# declaration_poc
def get_numero_agrement(item, _):
    numero_agrement = getattr(item, "numero_agrement", None)
    if numero_agrement is None:
        return "N/A"

    return numero_agrement


# demande
def get_motif(item, _):
    if getattr(item, "modification", None):
        return getattr(item.modification, "motif", "")
    return ""


def get_valide_manager_oc(item, _):
    if getattr(item, "valide_manager_oc", False) or (
            not getattr(item, "valide_manager_oc", False) and getattr(item, "motif",
                                                                      None) is not None):
        return "Fini"
    elif getattr(item, "valide_oc", False) or (
            not getattr(item, "valide_oc", False) and getattr(item, "motif_oc_decision", None) is not None):
        return "Valider fiche OP - niv2"
    else:
        return "Valider fiche OP - niv1"


# operation achat view
def get_pm(item, _):
    return f'{getattr(item, "pm_raison_sociale", "")}, {getattr(item, "pm_registre_commerce", "")}, {getattr(item, "pm_centre", "")}'


def get_poc(item, _):
    return f'{getattr(item, "poc_id", "")}, {getattr(item, "poc_denomination", "")}, {getattr(item, "poc_numero_agrement", "")}'


# ep functions
def get_apa_actif(item, _):
    return getattr(item, "apa_actif", 0) + getattr(item, "apna_actif", 0)


def get_m_actif(item, _):
    return getattr(item, "m_actif", 0)


def get_ama_actif(item, _):
    # item.ama_actif + item.amna_actif
    return getattr(item, "ama_actif", 0) + getattr(item, "amna_actif", 0)


# scd functions
def get_affiliation_group(item, _):
    if getattr(item, "affiliation_group", None):
        return item.affiliation_group.name
    return ""


# pm functions
def get_lieu_implantation_label(item, _):
    if getattr(item, "lieu_implantation", None):
        return item.lieu_implantation.label
    return ""


def get_categorie_op(item, _):
    if item.get("scd_id"):
        return "Scd"
    elif item.get("esd_id"):
        return "Esd"
    elif item.get("mandataire_id"):
        return "Mandataire"
    elif item.get("ep_id"):
        return "Ep"
    else:
        return "N/A"


def get_pm_id(item, _):
    return getattr(item, "mandataire_id", "") or getattr(item, "scd_id", "") or getattr(item, "esd_id", "") or getattr(
        item, "ep_id", "")


# pp functions
def get_poc_id(item, _):
    return getattr(item, "poc_id", "")


def get_designation_agence(item, _):
    if getattr(item, "poc", None):
        return getattr(item.poc, "nom_agence", "")
    return ""


def get_pp_field_name(item, field_name):
    if getattr(item, "esd", None):
        ite = item.esd
    elif getattr(item, "ep", None):
        ite = item.ep
    elif getattr(item, "poc", None) and getattr(item.poc, "mandataire", None):
        ite = item.poc.mandataire
    elif getattr(item, "poc", None) and getattr(item.poc, "ep", None):
        ite = item.poc.ep
    elif getattr(item, "representant", None) and getattr(item.representant, "scd", None):
        ite = item.representant.scd
    elif getattr(item, "scd", None):
        ite = item.scd
    else:
        ite = None

    if ite:
        return getattr(ite, field_name)
    else:
        return ""

# poc

def get_lieu_implantation_label_for_poc(item, _):
    if item.get("lieu_implantation"):
        return item.get("lieu_implantation").label
    return ""