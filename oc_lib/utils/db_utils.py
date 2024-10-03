from oc_lib.db import db


def find_class_by_table_name(table_name):
    # Find the class by table name
    for cls in db.Model._decl_class_registry.values():
        if hasattr(cls, '__tablename__') and cls.__tablename__ == table_name:
            return cls
    return None


def get_all_table_column_names(model):
    column_names = []

    # Get all columns from parent classes
    for cls in model.__mro__:
        if hasattr(cls, '__table__'):
            column_names.extend([column.name for column in cls.__table__.columns if column.name not in column_names])

    return column_names
