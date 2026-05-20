from .registry import registry
def get_provenance_debt(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("debt_score", 0) if obj else 0
