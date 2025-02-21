from oc_lib.utils.exceptions import NotFoundError

FUNCTION_REGISTRY = {}

def register_function(name, func):
    """Register a function in the registry"""
    FUNCTION_REGISTRY[name] = func

def get_registered_function(name):
    ret = FUNCTION_REGISTRY.get(name, None)
    if not ret:
        raise NotFoundError("No function registred with that name")
    return ret