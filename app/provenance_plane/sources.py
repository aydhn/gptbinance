from .registry import registry
def get_authoritative_sources():
    sources = []
    for obj in registry.list_all():
        if obj.get("class_type") == "source" and obj.get("source_authority") == "authoritative":
            sources.append(obj)
    return sources
