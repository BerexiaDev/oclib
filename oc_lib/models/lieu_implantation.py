from oc_lib.repository import Repository
from oc_lib.db import db

# add code as integer
# change lieu_implantation to label
# add default date to creation_date
# add unicty rule on code and label


class LieuImplantation(db.Model, Repository):
    """ Model pour paramétrage lieu implantation """
    id = db.Column(db.Integer, primary_key=True)
    lieu_implantation = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.Date, nullable=False)
    modification_date = db.Column(db.Date, nullable=False)
    