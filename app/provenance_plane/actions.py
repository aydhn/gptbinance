from .registry import registry
def check_action_lineage(action_id: str):
    obj = registry.get(action_id)
    return bool(obj and obj.get("action_type"))
