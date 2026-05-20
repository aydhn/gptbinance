from typing import Dict, Any, List
from .exceptions import InvalidProvenanceObject

class CanonicalProvenanceRegistry:
    def __init__(self):
        self.objects = {}

    def register(self, obj_id: str, data: Dict[str, Any]):
        if "provenance_id" not in data:
            raise InvalidProvenanceObject("Missing provenance_id")
        self.objects[obj_id] = data

    def get(self, obj_id: str) -> Dict[str, Any]:
        return self.objects.get(obj_id)

    def list_all(self) -> List[Dict[str, Any]]:
        return list(self.objects.values())

registry = CanonicalProvenanceRegistry()
