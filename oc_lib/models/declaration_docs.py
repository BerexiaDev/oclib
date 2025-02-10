from oc_lib.repository import Repository
from oc_lib.db import db
from sqlalchemy import text


class DeclarationDocs(db.Model, Repository):
    id = db.Column(db.Integer, primary_key=True)
    declaration_fiscal_id = db.Column(db.Integer, db.ForeignKey("declaration_fiscal.id"), nullable=False)
    intitule_document = db.Column(db.String(1000), nullable=False)
    nom_fichier = db.Column(db.String(1000), nullable=False, unique=True)
    date_creation = db.Column(db.Date, default=db.func.now())
    full_path= db.Column(db.String(250))

    # 1. Only PDF format allowed
    file_extension = db.Column(db.String(5), nullable=False)
    file_extension_check = db.CheckConstraint(text("file_extension IN ('PDF')"))

    # 2. One document per intitulé_document
    unique_document_per_intitule = db.UniqueConstraint(
        'declaration_fiscal_id', 'intitule_document'
    )

