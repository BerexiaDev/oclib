from enum import Enum


class Roles(Enum):
    OC_MANAGER = "OC_MANAGER"
    OC_ADMIN = "OC_ADMIN"
    OC_AGENT = "OC_AGENT"
    OC_SUPER_ADMIN = "OC_SUPER_ADMIN"
    OP = "OP"

    @classmethod
    def get_oc_roles(cls):
        return [cls.OC_MANAGER.value, cls.OC_ADMIN.value, cls.OC_AGENT.value, cls.OC_SUPER_ADMIN.value]
