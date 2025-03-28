from functools import wraps
import traceback
from oc_lib.utils.exceptions import InvalidDataError, UnauthorizedError, NotFoundError, AlreadyExistsError, \
    DateValidationError, PermissionDeniedError
from werkzeug.exceptions import NotFound
from loguru import logger
from psycopg2.errors import NotNullViolation, IntegrityError

from oc_lib.db import db


def catch_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFound:
            return {"status": "error", "message": "Non trouvé"}, 404
        except NotFoundError as e:
            return {"status": "error", "message": str(e)}, 404
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}, 400
        except (NotNullViolation, DateValidationError, InvalidDataError) as e:
            logger.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}, 400
        except PermissionDeniedError as e:
            logger.error(f"Permission denied error: {e}")
            return {"status": "error", "message": str(e)}, 403
        except Exception as e:
            args = getattr(e, "args")

            # Check if the exception is an IntegrityError, e.g: NotNullViolation or UniqueViolation or ForeignKeyViolation
            if args and len(args) > 0:
                if isinstance(args[0], IntegrityError):
                    sub_args = getattr(args[0], "args")
                    if sub_args and len(sub_args) > 0:
                        return {
                            "status": "error",
                            "message": sub_args[0],
                        }, 400

            traceback.print_exc()
            logger.error(f"Error {func.__name__}: {e}")
            return {
                "status": "error",
                "message": "Quelque chose s'est mal passé",
            }, 500

    return wrapper

def exception_handler(message=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except InvalidDataError as e:
                db.session.rollback()

                return {"status": "error", "message": e.message}, 400
            
            except UnauthorizedError as e:
                db.session.rollback()

                return {"status": "error", "message": e.message}, 401
            
            except NotFoundError as e:
                db.session.rollback()

                return {"status": "error", "message": e.message}, 404
            
            except AlreadyExistsError as e:
                db.session.rollback()

                return {"status": "error", "message": e.message}, 409
            
            except Exception as e:
                db.session.rollback()

                logger.error(f"Error in {func.__name__}: {e}")
                return {
                    "status": "error",
                    "message": message or "Erreur lors de l'exécution de l'opération",
                }, 500

        return wrapper
    return decorator