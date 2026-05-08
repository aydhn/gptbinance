from app.config_plane.models import ConfigParameterRef
from app.config_plane.enums import LayerClass, MutabilityClass
from app.config_plane.schemas import registry as schema_registry
from app.config_plane.mutability import validate_mutability


def request_runtime_patch(domain_str: str, name_str: str, value: any) -> dict:
    """
    Creates a patch intent request. Validates if the parameter is allowed to be patched at runtime.
    """
    domain = None
    from app.config_plane.enums import ConfigDomain

    for d in ConfigDomain:
        if d.value == domain_str:
            domain = d
            break

    if not domain:
        raise ValueError(f"Unknown domain {domain_str}")

    param = schema_registry.get_parameter(domain, name_str)
    if not param:
        raise ValueError(f"Unknown parameter {domain_str}.{name_str}")

    # Validation step: Can this be patched?
    validate_mutability(param.mutability_class, LayerClass.RUNTIME_SAFE_PATCH_INTENT)

    return {
        "status": "patch_intent_created",
        "parameter": f"{domain_str}.{name_str}",
        "new_value": value,
    }
