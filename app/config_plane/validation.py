from typing import Any
from app.config_plane.models import ConfigParameter
from app.config_plane.exceptions import InvalidParameterDefinition

def validate_type(value: Any, expected_type_name: str) -> bool:
    if expected_type_name == "bool":
        return isinstance(value, bool)
    elif expected_type_name == "int":
        return isinstance(value, int)
    elif expected_type_name == "float":
        return isinstance(value, float) or isinstance(value, int)
    elif expected_type_name == "str":
        return isinstance(value, str)
    # Allow any for complex types for now
    return True

def validate_parameter_value(param: ConfigParameter, value: Any):
    if not validate_type(value, param.type_name):
        raise InvalidParameterDefinition(f"Value {value} is not of type {param.type_name}")
