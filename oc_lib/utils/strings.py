from datetime import datetime
import importlib


def get_class_instance(module_name, class_name):
    module = importlib.import_module(module_name)
    return getattr(module, class_name)


def date_now():
    return datetime.date(datetime.now())

def timestamp():
    return datetime.now()

def update_element(data, element, non_editable_attrs=None):

    non_editable_attrs = non_editable_attrs or []
    for key, value in data.items():
        if key not in non_editable_attrs:
            setattr(element, key, value)
    return element


def convert_str_to_date(value):
    return datetime.date(datetime.strptime(value, "%Y-%m-%d"))


def current_year():
    return str(datetime.now().year)
