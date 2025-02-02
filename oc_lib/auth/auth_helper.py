from datetime import datetime
from flask import g
from oc_lib.models import User, Poc
from oc_lib.utils.constants import Roles
from oc_lib.utils.strings import date_now

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


    @staticmethod
    def handle_prepose_first_connection():
        if g.user.role == Roles.PREPOSE.value and g.user.poc_id and not g.user.first_connection_date:
            today_date = datetime.utcnow()
            g.user.first_connection_date = today_date

            poc = Poc.find_one(id=g.user.poc_id, date_debut_activite=None)
            if poc:
                poc.date_debut_activite = date_now()
                poc.save()

            g.user.save()