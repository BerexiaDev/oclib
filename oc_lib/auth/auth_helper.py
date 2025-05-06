from datetime import datetime
from flask import g
from oc_lib.models import User, Poc, Statut
from oc_lib.utils.constants import Roles
from oc_lib.db import db
from oc_lib.utils.funtion_registry import get_registered_function
from oc_lib.utils.strings import date_now, convert_str_to_date

class AuthHelper:
    @staticmethod
    def get_logged_in_user():
        keycloak_id = g.decoded_token['sub'].lower()
        if not isinstance(keycloak_id, str):
            return {"status": "fail", "message": "No Keycloak ID found"}, 400
        
        user = User.find_one(keycloak_id=keycloak_id)

        if not user:
            return {"status": "fail", "message": "No such user with the provided keycloak id"}, 404
        
        if user.role == Roles.PREPOSE.value and user.is_blocked == True:
            return {"statut": "fail", "message": "User is blocked"}, 403
               

        g.user = user

        return user, 200


    @staticmethod
    def handle_prepose_first_connection():
        if g.user.role == Roles.PREPOSE.value and g.user.poc_id and not g.user.first_connection_date:
            today_date = datetime.utcnow()
            g.user.first_connection_date = today_date

            poc = Poc.find_one(id=g.user.poc_id, date_debut_activite=None)
            if poc:
                poc.date_debut_activite = today_date
                poc.save()
                first_statut = db.session.query(Statut).filter(Statut.poc_id == g.user.poc_id, Statut.is_valid == True).order_by(Statut.id).first()
                if first_statut and convert_str_to_date(str(first_statut.date_delivrance)) > convert_str_to_date(str(poc.date_debut_activite.date())):
                    handle_create_notification = get_registered_function("handle_create_notification")
                    notif_params = {
                        "poc_id": poc.id,
                        "code": "NOTIF_011"
                    }
                    handle_create_notification(notif_params, is_mail=False)

            g.user.save()