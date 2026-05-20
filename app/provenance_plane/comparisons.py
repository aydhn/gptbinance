from .registry import registry
def compare_provenance(obj1_id: str, obj2_id: str):
    obj1 = registry.get(obj1_id)
    obj2 = registry.get(obj2_id)
    if not obj1 or not obj2: return False
    return obj1.get("lineage_refs") == obj2.get("lineage_refs")
