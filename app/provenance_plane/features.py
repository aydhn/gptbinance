from .registry import registry
def get_feature_lineage(feature_id: str):
    obj = registry.get(feature_id)
    return obj.get("lineage_refs", []) if obj else []
