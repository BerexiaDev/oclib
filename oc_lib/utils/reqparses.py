from flask_restx import reqparse


def export_table_data_reqparse():
    parser = reqparse.RequestParser()
    parser.add_argument("page", type=int, location="args")
    parser.add_argument("size", type=int, location="args")
    parser.add_argument("sort_key", type=str, location="args", default="id")
    parser.add_argument("sort_order", type=int, location="args", default=1)
    parser.add_argument("table_name", type=str, location="args", required=True)
    return parser
