from sqlalchemy import and_, or_, sql, func
from loguru import logger
from oc_lib.models.poc import Poc

tables_name_map = {
    "manager-pp": "gerant_pp",
    "manager-pm": "gerant_pm",
    "co-manager": "co_gerants",
    "representative": "representant",
    "suppleant": "suppleant",
    "partner-pm": "associe_pms",
    "partner-pp": "associe_pps",
    "agency": "guichets",
    "agrement": "agrements",
    "motif": "motifs",
    "mandataire": "mandataire",
    "poc_ss": "poc_ss",
    "poc_p": "poc_p",
    "modification-setting": "modification",
    "pattern": "pattern",
    "sous_operation": "sous_operation",
    "cancel_deadline": "cancel_deadline",
    "lieu_implantation": "lieu_implantation",
    "authorized_operation": "authorized_operation",
    "derogation_operation": "derogation_operation",
    "derogation_encaisse": "derogation_encaisse",
    "autorization_particuliere_pp": "autorization_particuliere_pp",
    "autorization_particuliere_pm": "autorization_particuliere_pm",
    "beneficiaire_pp": "beneficiaire_pp",
    "beneficiaire_pm": "beneficiaire_pm"
}


def build_operator(column, operator, value):
    if operator == "CONTAINS":
        return column.ilike(f"%{value}%")
    elif operator == "STARTS WITH":
        return column.ilike(f"{value}%")
    elif operator == "ENDS WITH":
        return column.ilike(f"%{value}")
    elif operator == "EQUALS":
        return column == value
    elif operator == "NOT EQUALS":
        return or_(column != value, column.is_(None))
    elif operator == "LESS THAN":
        return column < value
    elif operator == "GREATER THAN":
        return column > value
    elif operator == "BEFORE":
        return column < value
    elif operator == "AFTER":
        return column > value
    elif operator == "LESS EQUAL":
        return column <= value
    elif operator == "GREATER EQUAL":
        return column >= value
    elif operator == "IS NULL":
        return column.is_(None)
    elif operator == "IS NOT NULL":
        return column.isnot(None)
    elif operator == "ARRAY CONTAINS":
        conditions = [func.array_to_string(column, ' ').ilike(f"%{v.strip()}%") for v in value.split(',')]
        return or_(*conditions)
    else:
        return column == value


def format_criterias(criterias, main_table):
    output_data = {}
    for item in criterias:
        table_name, field_info = item.get("field", [None, {}])
        field_code = field_info.get("code", None)
        field_type = field_info.get("type", None)
        operator = item.get("operator", None)
        value = item.get("value", None)

        if not table_name:
            raise ValueError("No table name")
        if not field_code:
            raise ValueError("No columns name")
        if not field_type:
            raise ValueError("No field type")
        if not operator:
            raise ValueError("No operator")
        if value != 0 and not value:
            if operator not in ["IS NOT NULL", "IS NULL"]:
                raise ValueError("No value")

        if table_name not in output_data:
            output_data[table_name] = []

        output_data[table_name].append(
            {
                "code": field_code,
                "type": field_type,
                "operator": operator,
                "value": value,
            }
        )
    main_fields = output_data.pop(main_table, [])
    criterias = [
        {"table": table_name, "fields": fields}
        for table_name, fields in output_data.items()
    ]
    return main_fields, criterias


def build_conditions(table, fields, is_class=False):
    opertions = []
    for f in fields:
        if is_class:
            column = getattr(table, f["code"], None)
        else:
            column = getattr(table.property.mapper.class_, f["code"], None)

        if not column:
            logger.error(f"Non internal column for {f['code']}")
            raise ValueError(f"Non internal column for {f['code']}")

        operation = build_operator(column, f["operator"], f["value"])
        opertions.append(operation)

    return opertions


def build_filters(entity_class, query, search_criteria, main_table):
    main_fields, criterias = format_criterias(search_criteria, main_table)
    # Build conditions on main table
    main_conditions = build_conditions(entity_class, main_fields, is_class=True)
    query = query.filter(and_(*main_conditions))
    # Join related tables
    for criteria in criterias:
        try:
            table_name = criteria["table"]
            internal_table_name = tables_name_map.get(table_name, None)

            if not internal_table_name:
                logger.error(f"No internal name for table {table_name}")
                raise ValueError(f"No internal name for table {table_name}")

            table = getattr(entity_class, internal_table_name, None)

            if not table:
                logger.error(f"No  table attr {internal_table_name}")
                raise ValueError(f"No internal name for table {internal_table_name}")

            conditions = build_conditions(table, criteria["fields"])
            query = query.outerjoin(table).filter(and_(*conditions))

        except Exception as e:
            logger.error(f"Exception in build filters  {str(e)}")
            continue
    return query


# To refactor
def split_filters(filters):
    normal_filters = [f for f in filters if f["field"][1]["type"] != "special"]
    special_filters = [f for f in filters if f["field"][1]["type"] == "special"]
    return normal_filters, special_filters


def build_special_filters(query, filters):
    for filter in filters:
        try:

            code = filter["field"][1]["code"]
            value = filter["value"]
            operator = filter["operator"]

            if code == "pm":
                query = query_pm(value, operator, query)

            elif code == "categorie":
                query = query_category(value, operator, query)

        except Exception as e:
            logger.error(f"Exception in build filters  {str(e)}")

    return query


def query_pm(value, operator, query):

    if value == "ESD":
        if operator == "EQUALS":
            query = query.filter(Poc.esd_id != None)
        else:
            query = query.filter(Poc.esd_id == None)

    elif value == "SCD":
        if operator == "EQUALS":
            query = query.filter(Poc.scd_id != None)
        else:
            query = query.filter(Poc.scd_id == None)

    elif value == "EP":
        if operator == "EQUALS":
            query = query.filter(and_(Poc.ep_id != None, Poc.mandataire_id == None))
        else:
            query = query.filter(or_(Poc.ep_id == None, Poc.mandataire_id == None))

    elif value == "Mandataire":
        if operator == "EQUALS":
            query = query.filter(and_(Poc.ep_id != None, Poc.mandataire_id != None))
        else:
            query = query.filter(or_(Poc.ep_id == None, Poc.mandataire_id == None))
    else:
        query = query.filter(sql.false())

    return query


def query_category(value, operator, query):

    if value == "Point de change":
        if operator == "EQUALS":
            query = query.filter(or_(Poc.esd_id != None, Poc.scd_id != None))
        else:
            query = query.filter(and_(Poc.esd_id == None, Poc.scd_id == None))

    elif value == "Agence propre":
        if operator == "EQUALS":
            query = query.filter(and_(Poc.ep_id != None, Poc.mandataire_id == None))
        else:
            query = query.filter(or_(Poc.ep_id == None, Poc.mandataire_id != None))

    elif value == "Agence mandataire":
        if operator == "EQUALS":
            query = query.filter(and_(Poc.ep_id != None, Poc.mandataire_id != None))
        else:
            query = query.filter(or_(Poc.ep_id == None, Poc.mandataire_id == None))
    else:
        query = query.filter(sql.false())

    return query
