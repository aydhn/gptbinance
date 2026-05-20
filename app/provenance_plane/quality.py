from .registry import registry
def get_quality(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("quality_verdict", "UNKNOWN") if obj else "UNKNOWN"
