from .registry import registry
def query_provenance(obj_id: str):
    return registry.get(obj_id)
