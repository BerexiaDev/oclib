from oc_lib.db import db
from sqlalchemy.orm import aliased
from oc_lib.models.pp import Pp

def find_class_by_table_name(table_name):
    # Find the class by table name
    for cls in db.Model._decl_class_registry.values():
        if hasattr(cls, '__tablename__') and cls.__tablename__ == table_name:
            return cls
    return None

def validate_unique_active(class_name, current_instance):

    from oc_lib.models.gerant import Gerant
    from oc_lib.models.representant import Representant
    from oc_lib.models.suppleant import Suppleant
    # Create an alias for Pp
    PpAlias = aliased(Pp)

    is_gerant = isinstance(current_instance, Gerant)
    is_rep_sup = isinstance(current_instance, (Representant, Suppleant))
    #more models to be added

    filters = [
        PpAlias.statut.in_([True, None]),
        PpAlias.creation_status != 4
    ]

    # Add specific conditions based on the instance type
    if is_gerant:
        extra_conditions = class_name.scd_id == current_instance.scd_id if current_instance.scd_id else class_name.esd_id == current_instance.esd_id
    elif is_rep_sup:
        extra_conditions = class_name.scd_id == current_instance.scd_id
        
    filters.append(extra_conditions)

    active_instance = db.session.query(class_name).join(PpAlias).filter(*filters).first()

    if not active_instance:
        return True

    if is_gerant and active_instance:
        raise ValueError(
            "Il existe déjà un gerant actif pour cet opérateur."
        )
    elif is_rep_sup and (active_instance != current_instance):
        raise ValueError(
            "Il existe déjà un representant/suppleant actif pour cet opérateur."
        )
