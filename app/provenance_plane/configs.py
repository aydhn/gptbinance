from .registry import registry
def get_config_influence(config_id: str):
    obj = registry.get(config_id)
    return bool(obj and obj.get("is_active", False))
