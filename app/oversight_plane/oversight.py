from app.oversight_plane.models import OversightRecord
from app.oversight_plane.registry import oversight_registry

def create_oversight(oversight_id: str, owner: str, class_type: str="authoritative") -> OversightRecord:
    record = OversightRecord(
        oversight_id=oversight_id,
        class_type=class_type,
        owner=owner,
        scope_ref="full",
        scrutiny_posture="light",
        intervention_posture="advisory"
    )
    oversight_registry.register_oversight(record)
    return record
