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
    if getattr(item, "scd_id", None):
        return "Scd"
    elif getattr(item, "esd_id", None):
        return "Esd"
    elif getattr(item, "mandataire_id", None):
        return "Mandataire"
    elif getattr(item, "ep_id", None):
        return "Ep"
    else:
        return "N/A"


def get_pm_id(item, _):
    return getattr(item, "mandataire_id", "") or getattr(item, "scd_id", "") or getattr(item, "esd_id", "") or getattr(item, "ep_id", "")


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
