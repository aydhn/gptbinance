from .registry import registry
def get_derived_artifact(artifact_id: str):
    obj = registry.get(artifact_id)
    if obj and obj.get("class_type") == "derived_artifact":
        return obj
    return {}
