import functools
import traceback

from werkzeug.exceptions import NotFound
from loguru import logger


def catch_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFound:
            return {"status": "error", "message": "Non trouvé"}, 404
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            return {"status": "error", "message": str(e)}, 400
        except Exception as e:
            traceback.print_exc()
            logger.error(f"Error {func.__name__}: {e}")
            return {
                "status": "error",
                "message": "Quelque chose s'est mal passé",
            }, 500

    return wrapper
