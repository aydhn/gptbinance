from .registry import registry
def get_model_influence(model_id: str):
    obj = registry.get(model_id)
    return obj.get("influence_strength", "UNKNOWN") if obj else "UNKNOWN"
