from typing import Dict, Any
from app.semantic_plane.models import SemanticObjectRef
from app.semantic_plane.enums import SemanticClass

class SemanticObjectManager:
    def __init__(self):
        self.authoritative_objects: Dict[str, SemanticObjectRef] = {}

    def register_object(self, obj: SemanticObjectRef):
        self.authoritative_objects[obj.semantic_id] = obj
