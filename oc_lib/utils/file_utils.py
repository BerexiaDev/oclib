import hashlib
import datetime
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import current_app as app

mime_types = {
    "pdf": "application/pdf",
    "txt": "text/plain",
    "csv": "text/csv",
    "doc": "application/msword",
    "jpeg": "image/jpeg",
    "jpg": "image/jpeg",
    "png": "image/png",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "xls": "application/vnd.ms-excel",
    "ppt": "application/vnd.ms-powerpoint",
    "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
}



def allowed_file(filename, allowed_extensions: set):
    file_extension = filename.rsplit('.', 1)[-1].lower()

    if '.' in filename and file_extension in allowed_extensions:
        return file_extension


def generate_file_id(token):
    """Generates a unique hashed id for token based on timestamp"""

    timestamp = f"{str(datetime.datetime.now().date())}_{str(datetime.datetime.now().time()).replace(':', '.')}"
    token = f"{secure_filename(token)}_{timestamp}"

    return f"{hashlib.sha256(token.encode('utf-8')).hexdigest()}"


def get_path(folder, import_folder: str, filename="", extension="pdf", as_folder=False, create=False):
    """Creates the full path for a file under UPLOAD FOLDER"""
    folder_path = Path(get_upload_file_path(import_folder=import_folder, folder=folder))
    if create:
        folder_path.mkdir(parents=True, exist_ok=True)
    if as_folder:
        return str(folder_path)
    else:
        return str(folder_path.joinpath(f"{filename}.{extension}"))


def get_upload_file_path(import_folder, folder=""):
    """constructs the full path for a file under UPLOAD FOLDER """
    upload_path = Path(app.config["UPLOAD_FOLDER"] + "/" + import_folder)
    return upload_path.joinpath(folder)


def check_file_and_extension(file, allowed_extensions):
    if not file or not file.filename:
        raise ValueError("Aucun fichier trouvé")

    file_extension = allowed_file(file.filename, allowed_extensions=allowed_extensions)

    if not file_extension:
        raise ValueError("Format de fichier non accepté")
    return file_extension
