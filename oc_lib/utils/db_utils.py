from oc_lib.db import db


def find_class_by_table_name(table_name):
    # Find the class by table name
    for cls in db.Model._decl_class_registry.values():
        if hasattr(cls, '__tablename__') and cls.__tablename__ == table_name:
            return cls
    return None
