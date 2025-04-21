from functools import wraps
from flask import request, g
from oc_lib.auth.keycloak_auth import KeycloakAuth
from oc_lib.auth.auth_helper import AuthHelper


IGNORE_PATHS = ["/", "/swagger.json"]
NOTIFICATION_CREATION_PATH = "/notifications"

def decode_jwt(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(request.path)
        if request.path in IGNORE_PATHS or "swagger" in request.path:
            return f(*args, **kwargs)
        
        elif request.path == NOTIFICATION_CREATION_PATH and request.headers.get('X-NotifCreation', "false") == "true":
            return f(*args, **kwargs)
        try:
            # Decode token and store it in the global scope
            g.decoded_token = KeycloakAuth.decode_token()
            
            # Retrieve logged-in user data
            data, status = AuthHelper.get_logged_in_user()

            if status != 200:
                g.decoded_token = None
                return data, status

            AuthHelper.handle_prepose_first_connection()

        except Exception as e:
            return {"status": "fail", "message": str(e)}, 401
        
        return f(*args, **kwargs)
    return decorated_function