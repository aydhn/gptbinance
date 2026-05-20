from .registry import registry
def get_outcome_lineage(outcome_id: str):
    obj = registry.get(outcome_id)
    return obj.get("lineage_refs", []) if obj else []
