import io
import csv

import pandas as pd
import importlib

from io import BytesIO
from datetime import datetime
from flask import send_file, g
from sqlalchemy import asc, desc

from oc_lib.utils.decorators import exception_handler
from oc_lib.utils.exceptions import UnauthorizedError, InvalidDataError
from oc_lib.utils.filter import build_filters
from oc_lib.utils.excel_utils import auto_adjust_column_width, set_data_sheet
from oc_lib.utils.export_table_data_constants import EXPORT_TABLE_INFO
from oc_lib.utils.export_table_data_func import get_users_list


def get_function_from_path(module_path, function_name):
    module = importlib.import_module(module_path)
    return getattr(module, function_name)


@exception_handler(message="Erreur lors de l'exportation des données du tableau")
def export_tables(args, request_body):
    sort_key = args.get("sort_key")
    sort_order = args.get("sort_order")
    table_name = args.get("table_name")
    file_type = args.get("file_type")
    column_ids = request_body.get("columns", [])

    # Check if the user has permission to export the table
    values_mapping, columns, func_path, func_name, is_multiple_sort = _check_permission_and_return_values_mapping_and_column_name(
        table_name)

    column_names = _validate_column_ids(column_ids, columns)

    if table_name == "user":
        all_result = get_users_list(args)
    else:
        func_ins = get_function_from_path(func_path, func_name)
        if is_multiple_sort:
            if not isinstance(sort_key, list):
                sort_key = [sort_key]
            if not isinstance(sort_order, list):
                sort_order = [sort_order]

        all_result = func_ins({**args, "sort_key": sort_key, "sort_order": sort_order}, request_body, True)
    data = []
    for d in all_result:
        each_data = []
        for col_id in column_ids:
            col_info = columns.get(col_id)
            if isinstance(col_info, str):
                try:
                    each_data.append(getattr(d, col_id))
                except AttributeError:
                    each_data.append(d.get(col_id))
            else:
                func = col_info.get("func")
                each_data.append(func(d, col_id))
        data.append(each_data)

    rows_data = _generate_rows_data(column_ids, data, values_mapping)
    return _excel_export(table_name, column_names, rows_data, file_type)


def _validate_column_ids(column_ids, columns):
    column_names = []
    for c in column_ids:
        if c in columns:
            column_name = columns.get(c) if isinstance(columns.get(c), str) else columns.get(c).get("title")
            column_names.append(column_name)

    return column_names


def _check_permission_and_return_values_mapping_and_column_name(table_name):
    table_info = EXPORT_TABLE_INFO.get(table_name)

    if table_info:
        required_roles = table_info.get("required_roles")
        if required_roles is not None and g.user.role not in required_roles:
            raise UnauthorizedError("Vous n'êtes pas autorisé à exporter les données de cette table.")

        return table_info.get("values_mapping", {}), table_info.get("columns", {}), table_info.get(
            "func_path"), table_info.get("func_name"), table_info.get("is_multiple_sort", False)

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
        return mapping_value.get(val, "")
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
