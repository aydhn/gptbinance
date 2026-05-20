from .registry import registry
def get_input_lineage(input_id: str):
    obj = registry.get(input_id)
    if not obj:
        return []
    return obj.get("lineage_refs", [])
