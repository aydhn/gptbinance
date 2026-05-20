from .registry import registry
def store_provenance_object(obj_id: str, data: dict):
    registry.register(obj_id, data)
    return True
