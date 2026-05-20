from .registry import registry
def get_provenance_readiness(obj_id: str):
    obj = registry.get(obj_id)
    return bool(obj and obj.get("is_ready", False))
