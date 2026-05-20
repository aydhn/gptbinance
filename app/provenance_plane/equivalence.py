from .registry import registry
def get_equivalence(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("equivalence_verdict", "UNKNOWN") if obj else "UNKNOWN"
