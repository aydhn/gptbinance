from .registry import registry
def forecast_provenance_decay(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("decay_forecast", "STABLE") if obj else "UNKNOWN"
