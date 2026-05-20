from .registry import registry
def check_approval_lineage(approval_id: str):
    obj = registry.get(approval_id)
    return bool(obj and obj.get("approved_by"))
