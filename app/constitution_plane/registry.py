from typing import Dict, List
from app.constitution_plane.models import ConstitutionObject
from app.constitution_plane.exceptions import ConstitutionStorageError

class CanonicalConstitutionRegistry:
    def __init__(self):
        self._objects: Dict[str, ConstitutionObject] = {}

    def register(self, obj: ConstitutionObject):
        if not obj.constitution_id:
            raise ConstitutionStorageError("Constitution object missing ID.")
        self._objects[obj.constitution_id] = obj

    def get(self, constitution_id: str) -> ConstitutionObject:
        return self._objects.get(constitution_id)

    def get_all(self) -> List[ConstitutionObject]:
        return list(self._objects.values())
