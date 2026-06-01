from app.assurance_plane.models import AssuranceObject
from app.assurance_plane.enums import AssuranceClass

def create_assurance_object(assurance_id: str, owner: str, class_type: AssuranceClass, scope_refs: list[str]) -> AssuranceObject:
    return AssuranceObject(
        assurance_id=assurance_id,
        owner=owner,
        class_type=class_type,
        scope_refs=scope_refs
    )
