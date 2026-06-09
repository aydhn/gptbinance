from typing import Dict, Any
from app.oversight_plane.models import OversightObjectRef

def build_oversight_object(oversight_id: str, object_type: str) -> OversightObjectRef:
    return OversightObjectRef(oversight_id=oversight_id, object_type=object_type)
