from app.indemnity_plane.models import IndemnityObject
def create_indemnity_object(id: str, class_type: str, owner: str, scope: str) -> IndemnityObject:
    return IndemnityObject(id=id, class_type=class_type, owner=owner, scope=scope)
