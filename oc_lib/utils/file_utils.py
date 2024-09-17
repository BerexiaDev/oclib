import hashlib
import datetime
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import current_app as app

ALLOWED_EXTENSIONS = {"pdf"}
IMPORT_LIASSE_FOLDER = "liasse/"


def allowed_file(filename):
    file_extension = filename.rsplit('.', 1)[-1].lower()

    if '.' in filename and file_extension in ALLOWED_EXTENSIONS:
        return file_extension


def generate_file_id(token):
    """Generates a unique hashed id for token based on timestamp"""

    timestamp = f"{str(datetime.datetime.now().date())}_{str(datetime.datetime.now().time()).replace(':', '.')}"
    token = f"{secure_filename(token)}_{timestamp}"

    return f"{hashlib.sha256(token.encode('utf-8')).hexdigest()}"


def get_path(folder, filename="", extension="pdf", as_folder=False, create=False):
    """Creates the full path for a file under UPLOAD FOLDER"""

    folder_path = Path(get_upload_file_path(folder=folder))
    if create:
        folder_path.mkdir(parents=True, exist_ok=True)
    if as_folder:
        return str(folder_path)
    else:
        return str(folder_path.joinpath(f"{filename}.{extension}"))


def get_upload_file_path(folder=""):
    """constructs the full path for a file under UPLOAD FOLDER """

    upload_path = Path(app.config['UPLOAD_FOLDER'] + "/" + (IMPORT_LIASSE_FOLDER))
    return upload_path.joinpath(folder)
