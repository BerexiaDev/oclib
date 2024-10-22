import io
import csv

import pandas as pd

from io import BytesIO
from datetime import datetime
from flask import send_file, g
from sqlalchemy import asc, desc

from oc_lib.utils.decorators import exception_handler
from oc_lib.utils.exceptions import UnauthorizedError
from oc_lib.utils.filter import build_filters
from oc_lib.utils.db_utils import find_class_by_table_name
from oc_lib.utils.excel_utils import auto_adjust_column_width, set_data_sheet
from oc_lib.utils.export_table_data_constants import EXPORT_TABLE_INFO


@exception_handler(message="Erreur lors de l'exportation des données du tableau")
def export_tables(args, filter_data):
    sort_key = args.get("sort_key")
    sort_order = args.get("sort_order")
    table_name = args.get("table_name")
    file_type = args.get("file_type")

    model_class = find_class_by_table_name(table_name)
    if not model_class:
        raise ValueError(f"Table {table_name} not found")

    # Check if the user has permission to export the table
    values_mapping, columns = _check_permission_and_return_values_mapping_and_column_name(table_name)

    attrs = [getattr(model_class, column_name) for column_name in columns.keys()]

    query = model_class.query.with_entities(*attrs)

    query = build_filters(model_class, query, filter_data.get("filters", []), table_name)
    query = query.order_by(asc(sort_key) if sort_order == 1 else desc(sort_key))

    data = query.all()

    column_ids = list(columns.keys())
    column_names = list(columns.values())

    rows_data = _generate_rows_data(column_ids, data, values_mapping)
    return _excel_export(table_name, column_names, rows_data, file_type)


def _check_permission_and_return_values_mapping_and_column_name(table_name):
    table_info = EXPORT_TABLE_INFO.get(table_name)

    if table_info:
        required_roles = table_info.get("required_roles", [])
        if g.user.role not in required_roles:
            raise UnauthorizedError("Vous n'êtes pas autorisé à exporter les données de cette table.")

        return table_info.get("values_mapping", {}), table_info.get("columns", {})

    raise UnauthorizedError("Vous n'êtes pas autorisé à exporter les données de cette table.")


def _generate_rows_data(table_columns, data, values_mapping):
    rows_data = []
    for each_row in data:
        row_data = []
        for ind, cel in enumerate(each_row):
            val = _get_mapping_value(table_columns[ind], cel, values_mapping)
            row_data.append(val)
        rows_data.append(row_data)

    return rows_data


def _get_mapping_value(column_name, val, values_mapping):
    mapping_value = values_mapping.get(column_name)
    if mapping_value:
        return mapping_value.get(val, val)
    elif isinstance(val, datetime):
        return val.strftime("%Y-%m-%d %H:%M:%S")
    elif val is None:
        return ""
    else:
        return str(val)


def _excel_export(table_name, columns, data, file_type):
    date_str = datetime.now().strftime("%Y-%m-%d")

    if file_type == "csv":
        output = io.StringIO()
        writer = csv.writer(output)

        # Write CSV header
        writer.writerow(columns)
        writer.writerows(data)

        # Move to the beginning of the StringIO buffer
        output.seek(0)

        # Send the file as a CSV download
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            attachment_filename=f'{table_name}_{date_str}.{file_type}',
        )

    else:
        output = BytesIO()
        # Initialize a new Excel workbook
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
            attachment_filename=f'{table_name}_{date_str}.{file_type}',
        )

    return response
