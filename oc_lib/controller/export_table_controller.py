from flask import request
from flask_restx import Resource

from oc_lib.services.export_table_data_service import export_tables
from oc_lib.utils.reqparses import export_table_data_reqparse
from oc_lib.utils.dto_utils import ExportTableDto

api = ExportTableDto.api
search_dto = ExportTableDto.search_dto


@api.route("")
class ExportTable(Resource):
    @api.doc(
        params={
            "sort_key":'sort key',
            "sort_order":"sort order (1 for asc -1 for desc)",
            "table_name":"table name",
            "file_type": "xslx",
        }
    )
    @api.expect(search_dto, validate=True)
    @api.response(200, "Export Done")
    def post(self):
        parser = export_table_data_reqparse()
        args = parser.parse_args()
        data = request.json
        return export_tables(args, data)
