from .registry import registry
def generate_manifest(obj_id: str):
    obj = registry.get(obj_id)
    return {"manifest_id": f"man_{obj_id}", "data": obj} if obj else {}
