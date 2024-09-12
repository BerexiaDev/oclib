from flask_restx import fields, Namespace


class NullableInteger(fields.Integer):
    __schema_type__ = ["integer", "null"]
    __schema_example__ = "nullable integer"


class NullableString(fields.String):
    __schema_type__ = ["string", "null"]
    __schema_example__ = "nullable string"


class NullableDatetime(fields.DateTime):
    __schema_type__ = ["string", "null"]
    __schema_example__ = "nullable Datetime"

class NullableDate(fields.Date):
    __schema_type__ = ["string", "null"]
    __schema_example__ = "nullable Date"
    
class NullableBoolean(fields.Boolean):
    __schema_type__ = ["boolean", "null"]
    __schema_example__ = "nullable Boolean"


class ErrorDto:
    api = Namespace("error", description="Error related operations")
    error = api.model(
        "error",
        {
            "status": fields.String(
                description="status", required=True, skip_none=True
            ),
            "message": fields.String(
                description="message", required=True, skip_none=True
            ),
        },
    )


class SearchDto:
    api = Namespace("Advanced Search", description="Advanced Search")
    
    search_dto = api.model(
        "Search criteria",
        {"filters": fields.List(fields.Raw(), required=True)},
    )