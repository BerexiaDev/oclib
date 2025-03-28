from oc_lib.utils.exceptions import NotFoundError

FUNCTION_REGISTRY = {}

def register_function(injected_functions):
    """Register a function in the registry"""
    for name, func in injected_functions.items():
        FUNCTION_REGISTRY[name] = func

def get_registered_function(name):
    ret = FUNCTION_REGISTRY.get(name, None)
    if not ret:
        raise NotFoundError("No function registred with that name")
    return ret