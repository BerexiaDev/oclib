from loguru import logger


def build_sort_column(model, field_path, query):
    if "." not in field_path:
        return field_path,query
    
    nested_field, subfield = field_path.split(".")
    attr = getattr(model, nested_field, None)

    if not hasattr(attr, "relationship"):
        try:
            related_model = attr.property.mapper.class_  #Finding related model from current model
            query = query.join(related_model)
            return getattr(related_model, subfield), query
        except AttributeError:
            logger.error(f"'{nested_field}' is not a relationship or valid _id field on {model.__name__}")
            raise ValueError(f"Erreur lors du tri par le champs: '{nested_field}'")

    #Attribute has another relationship to start on
    related_model = attr.relationship.property.mapper.class_
    logger.info(f"Calling build_sort_column recursively with model: {related_model.__name__}, subfield: {subfield}")
    return build_sort_column(related_model, subfield, query)