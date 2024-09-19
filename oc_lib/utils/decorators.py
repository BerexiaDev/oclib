from functools import wraps
import traceback
from oc_lib.utils.exceptions import InvalidDataError, UnauthorizedError, NotFoundError, AlreadyExistsError
from werkzeug.exceptions import NotFound
from loguru import logger


def catch_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFound:
            return {"status": "error", "message": "Non trouvé"}, 404
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}, 400
        except NotNullViolation as e:
            logger.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}, 400
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
                return { "status":"error", "message":e.message }, 400
            
            except UnauthorizedError as e:
                return { "status":"error", "message":e.message }, 401
            
            except NotFoundError as e:
                return { "status":"error", "message":e.message }, 404
            
            except AlreadyExistsError as e:
                return { "status":"error", "message":e.message }, 409
            
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {e}")
                return {
                    "status": "error",
                    "message": message or "Erreur lors de l'exécution de l'opération",
                }, 500

        return wrapper
    return decorator