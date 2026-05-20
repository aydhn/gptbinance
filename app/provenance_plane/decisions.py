from .registry import registry
def check_decision_lineage(decision_id: str):
    obj = registry.get(decision_id)
    return bool(obj and len(obj.get("lineage_refs", [])) > 0)
