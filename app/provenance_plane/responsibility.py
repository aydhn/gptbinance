from .registry import registry
def get_responsibility(obj_id: str):
    obj = registry.get(obj_id)
    return obj.get("accountable_actors", []) if obj else []
