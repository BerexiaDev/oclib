from oc_lib.db import db
from sqlalchemy.orm import aliased
from oc_lib.models.pp import Pp
from oc_lib.models.pm import Pm

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
    from oc_lib.models.gerant_pm import GerantPm
    # Create an alias for Pp
    PpAlias = aliased(Pp)
    GerantPmAlias = aliased(GerantPm)

    is_gerant = isinstance(current_instance, Gerant)
    is_rep_sup = isinstance(current_instance, (Representant, Suppleant))
    is_gerant_pm = isinstance(current_instance, GerantPm)
    #more models to be added

    filter_class = GerantPmAlias if is_gerant_pm else PpAlias 
    filters = [
        filter_class.creation_status != 4
    ]
    if is_gerant_pm:
        filters.append(filter_class.is_actif.in_([True, None]))
    else:
        filters.append(filter_class.statut.in_([True, None]))

    # Add specific conditions based on the instance type
    if is_gerant:
        extra_conditions = class_name.scd_id == current_instance.scd_id if current_instance.scd_id else class_name.esd_id == current_instance.esd_id
    elif is_rep_sup:
        extra_conditions = class_name.scd_id == current_instance.scd_id
    elif is_gerant_pm:
        extra_conditions = class_name.esd_id == current_instance.esd_id
        
    filters.append(extra_conditions)

    active_instance = db.session.query(class_name).join(filter_class).filter(*filters).first()

    if not active_instance:
        return True

    if is_gerant and (active_instance != current_instance):
        raise ValueError(
            "Il existe déjà un gerant actif pour cet opérateur."
        )
    elif is_rep_sup and (active_instance != current_instance):
        raise ValueError(
            "Il existe déjà un representant/suppleant actif pour cet opérateur."
        )
    elif is_gerant_pm and (active_instance != current_instance):
        raise ValueError(
            "Il existe déjà un gerant pm actif pour cet opérateur."
        )
