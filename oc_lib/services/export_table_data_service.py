import pandas as pd

from io import BytesIO
from datetime import datetime
from flask import send_file, g
from openpyxl.cell import MergedCell
from openpyxl.utils import get_column_letter
from sqlalchemy import asc, desc

from oc_lib.utils.decorators import exception_handler
from oc_lib.utils.exceptions import UnauthorizedError
from oc_lib.utils.filter import build_filters
from oc_lib.utils.db_utils import find_class_by_table_name, get_all_table_column_names
from oc_lib.utils.excel_utils import auto_adjust_column_width, set_data_sheet


@exception_handler(message="Erreur lors de l'exportation des données du tableau")
def export_tables(args, filter_data):
    sort_key = args.get("sort_key")
    sort_order = args.get("sort_order")
    size = args.get("size")
    page = args.get("page")
    table_name = args.get("table_name")
    model_class = find_class_by_table_name(table_name)

    # Check if the user has permission to export the table
    _check_permission(model_class)

    table_columns = get_all_table_column_names(model_class)

    query = build_filters(model_class, model_class.query, filter_data.get("filters", []), table_name)
    query = query.order_by(asc(sort_key) if sort_order == 1 else desc(sort_key))

    if size and page:
        pagination = query.paginate(page, size)
        data = pagination.items
    else:
        data = query.all()

    rows_data = _generate_rows_data(table_columns, data)
    return _excel_export(table_name, table_columns, rows_data)


def _check_permission(model_class):
    roles = []
    if hasattr(model_class, "ROLES_FOR_EXPORT"):
        roles = model_class.ROLES_FOR_EXPORT

    if roles and g.user.role not in roles:
        raise UnauthorizedError("Vous n'êtes pas autorisé à exporter les données de cette table.")


def _generate_rows_data(table_columns, data):
    rows_data = []
    for each_row in [d.to_dict() for d in data]:
        row_data = []
        for column_name in table_columns:
            val = each_row[column_name]
            if type(val) == datetime:
                val = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                val = str(val)
            row_data.append(val)
        rows_data.append(row_data)

    return rows_data


def _excel_export(table_name, columns, data):
    # Initialize a new Excel workbook
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        workbook = writer.book

        # Set up the Data sheet
        worksheet_data = workbook.create_sheet(table_name)
        set_data_sheet(worksheet_data, columns, data)
        auto_adjust_column_width(worksheet_data)

    # Set the buffer position to the beginning
    output.seek(0)
    response = send_file(
        output,
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        attachment_filename=f'{table_name}.xlsx',
    )

    return response
