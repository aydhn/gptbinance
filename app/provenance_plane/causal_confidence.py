from .registry import registry
def get_causal_confidence(outcome_id: str):
    obj = registry.get(outcome_id)
    return obj.get("causal_confidence", "LOW") if obj else "UNKNOWN"
