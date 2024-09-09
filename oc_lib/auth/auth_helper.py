from flask import g
from oc_lib.models.user import User

class AuthHelper:
    @staticmethod
    def get_logged_in_user():
        keycloak_id = g.decoded_token['sub'].lower()
        if not isinstance(keycloak_id, str):
            return {"status": "fail", "message": "No Keycloak ID found"}, 400
        
        user = User.find_one(keycloak_id=keycloak_id)

        if not user:
            return {"status": "fail", "message": "No such user with the provided keycloak id"}, 404

        g.user = user

        return user, 200
