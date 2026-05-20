from .registry import registry
def check_side_effects(action_id: str):
    obj = registry.get(action_id)
    return bool(obj and "side_effects" in obj)
