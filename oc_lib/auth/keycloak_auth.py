import requests, traceback, jwt

from flask import request
from flask import current_app as app, has_app_context


class KeycloakAuth:
    _instance = None
    keycloak_host = None
    jwks_uri = None
    keys = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KeycloakAuth, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def _initialize(cls):
        if not has_app_context():
            raise RuntimeError("Application context required for KeycloakAuth initialization")

        if cls._instance.keycloak_host is None:
            cls._instance.keycloak_host = app.config['KEYCLOAK_HOST']
            cls._instance.jwks_uri = f"{app.config['KEYCLOAK_HOST']}/realms/office-des-changes/protocol/openid-connect/certs"
            cls._instance.keys = cls._instance.fetch_public_keys()

    @classmethod
    def create_instance(cls):
        instance = cls.__new__(cls)
        instance._initialize()

    def fetch_public_keys(self):
        try:
            # TODO: remove verify false after setuping ssl
            response = requests.get(self.jwks_uri, verify=False)
            if response.status_code != 200:
                raise Exception("Failed to fetch public keys")
            
            return response.json()["keys"]
        except requests.exceptions.RequestException as e:
            traceback.print_exc()
            return None
        except Exception as e:
            traceback.print_exc()
            return None

    def get_token_auth_header(self):
        auth = request.headers.get("Authorization", None)
        if not auth:
            raise Exception("Authorization header is expected")

        parts = auth.split()

        if parts[0].lower() != "bearer":
            raise Exception("Authorization header must start with Bearer")

        elif len(parts) == 1:
            raise Exception("Token not found")

        elif len(parts) > 2:
            raise Exception("Authorization header must be Bearer token")

        token = parts[1]
        return token

    @classmethod
    def get_rsa_key(cls, token):
        cls.create_instance()

        if not cls._instance.keys:
            raise Exception("RSA keys not available")
        
        headers = jwt.get_unverified_header(token)
        try:
            for key in cls._instance.keys:
                if key["kid"] == headers["kid"]:
                    return key
            raise Exception("RSA key not found")

        except Exception:
            traceback.print_exc()
            raise Exception(f"Failed to get RSA key: {str(e)}")
        
    @classmethod
    def decode_token(cls):
        cls.create_instance()

        token = cls._instance.get_token_auth_header()
        rsa_key = cls._instance.get_rsa_key(token)
        
        try:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(rsa_key)
            unverified_payload = jwt.decode(token, options={"verify_signature": False})
            decoded_token = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                audience=unverified_payload.get("aud"),
            )
            return decoded_token
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError as e:
            raise Exception(f"Invalid token: {str(e)}")
        except Exception as e:
            raise Exception(f"Unable to parse token: {str(e)}")
