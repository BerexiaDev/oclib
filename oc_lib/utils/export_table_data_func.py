def get_poc_id(item, field_name):
    return getattr(item, "poc_id", "")


def get_designation_agence(item):
    if getattr(item, "poc_id", None):
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
