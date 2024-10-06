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
