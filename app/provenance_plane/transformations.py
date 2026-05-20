from .registry import registry
from .exceptions import InvalidTransformation
def handle_transformation(transform_id: str):
    obj = registry.get(transform_id)
    if not obj or obj.get("class_type") != "transformation":
        raise InvalidTransformation(f"Invalid transformation {transform_id}")
    return True
