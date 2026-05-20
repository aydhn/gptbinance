from .registry import registry
def get_divergence(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("divergence_severity", "UNKNOWN") if obj else "UNKNOWN"
