from enum import Enum

class Roles(Enum):
    OC_ADMIN = "OC_ADMIN"
    OC_SUPER_ADMIN = "OC_SUPER_ADMIN"
    OC_AGENT = "OC_AGENT"
    OC_MANAGER = "OC_MANAGER"
    OP = "OP"
    PREPOSE = "PREPOSE"
    AGENT_AUTORISATION = "AGENT_AUTORISATION"
    MANAGER_AUTORISATION = "MANAGER_AUTORISATION"

    @classmethod
    def get_oc_roles(cls):
        return [cls.OC_MANAGER.value, cls.OC_ADMIN.value, cls.OC_AGENT.value, cls.OC_SUPER_ADMIN.value]


class TypeOperation(Enum):
    ACHAT = 1
    VENTE = 2
    CESSION = 3


Type_Operation_MAPPING = {
    1: "Achat",
    2: "Vente",
    3: "Cession"
}


QUALITE_BENEFICIAIRE_MAPPING = {
    1: "PM-Résident",
    2: "PM-Non Résident",
    3: "PP-Etranger non Résident",
    4: "PP-Etranger Résident",
    5: "PP-Marocain Résident",
    6: "PP-Marocain non résident (MRE)",
    7: "Point de change",
}

CATEGORIE_PC_MAPPING = {
    1: "Société de change de devises",
    2: "Etablissement de paiement – Agences propres agréée",
    3: "Etablissement de paiement – Agences propres non-agréée",
    4: "Etablissement de paiement – Agences Mandataires agréée",
    5: "Etablissement de paiement – Agences Mandataires non-agréée",
    6: "Etablissement Sous Délégataire",
    7: "Banque"
}

STATUT_MAPPING = {
    1: "Enregistrée",
    2: "Annulée"
}

YES_NO_MAPPING = {
    True: "Oui",
    False: "Non"
}

CREATION_STATUS_MAPPING = {
    0: "En cours de saisi",
    1: "Validé",
    2: "En cours de validation",
    3: "En cours de demande modification",
    4: "Rejeté"
}

PM_TYPE_MAPPING = {
    "associe_pm": "Associé",
    "ep": "Ep",
    "esd": "Esd",
    "gerantpm": "Gérant",
    "mandataire": "Mandataire",
    "scd": "Scd"
}
