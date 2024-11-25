import re
from datetime import date

from oc_lib.utils.exceptions import InvalidDataError

NUMERO_DECISION_PATTERN = r"^[a-zA-Z0-9]{1,6}/[1-9]\d{0,4}/\d{4}$"
CIM_PATTERN = r"^[A-Z]{1,2}\d{1,6}[A-Z]{1,2}$"
CNI_PATTERN = r"^[A-Z]{1,2}\d{1,6}$"
NORMAL_PATTERN = r"^[a-zA-Z0-9]*$"


def validate_numero_decision(key, value, error_msg=None):
    """
        texte : max 6 cara avec min de 1
        Chiffre : max 5 cara avec min de 1 ( de 1 à 99 999)
        Chiffre : 4 caractères (année) (Année en cours et moins)
    """

    if not value:
        return value

    error_msg = error_msg if error_msg else f"Format de {key} non valide"
    if not re.match(NUMERO_DECISION_PATTERN, value):
        raise InvalidDataError(error_msg)

    # check the third part is a valid year and less than this year
    year = int(value.split("/")[-1])
    if year > date.today().year:
        raise InvalidDataError(error_msg)
    return value


def validate_cni(key, value, error_msg=None):
    """
        La CIN doit comporter 1 à 2 lettres majuscules suivies de 1 à 6 chiffres
    """

    if not value:
        return value

    error_msg = error_msg if error_msg else f"Format de {key} non valide"

    if not re.match(CNI_PATTERN, value):
        raise InvalidDataError(error_msg)

    return value

def validate_cim(key, value, error_msg=None):
    """
        La CIN doit comporter 1 à 2 lettres majuscules suivies de 1 à 6 chiffres, suivie d'un 1 à 2 lettres majuscules
    """
    if not value:
        return value

    error_msg = error_msg if error_msg else f"Format de {key} non valide"

    if not re.match(CIM_PATTERN, value):
        raise InvalidDataError(error_msg)

    return value


def validate_normal_pattern(key, value, error_msg=None):
    if not value:
        return value

    error_msg = error_msg if error_msg else f"Format de {key} non valide"

    if not re.match(NORMAL_PATTERN, value):
        raise InvalidDataError(error_msg)

    return value
