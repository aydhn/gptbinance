from .registry import registry
def get_contributions(outcome_id: str):
    obj = registry.get(outcome_id)
    return obj.get("contributing_factors", []) if obj else []
