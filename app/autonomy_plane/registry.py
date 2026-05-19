from typing import Dict, List, Optional
from app.autonomy_plane.models import AutonomyObject
from app.autonomy_plane.enums import AutonomyClass

class CanonicalAutonomyRegistry:
    def __init__(self):
        self._objects: Dict[str, AutonomyObject] = {}

    def register(self, obj: AutonomyObject) -> None:
        if not obj.autonomy_id:
            raise ValueError("No undocumented autonomy ids allowed.")
        self._objects[obj.autonomy_id] = obj

    def get(self, autonomy_id: str) -> Optional[AutonomyObject]:
        return self._objects.get(autonomy_id)

    def list_all(self) -> List[AutonomyObject]:
        return list(self._objects.values())

    def get_by_class(self, autonomy_class: AutonomyClass) -> List[AutonomyObject]:
        return [obj for obj in self._objects.values() if obj.autonomy_class == autonomy_class]

registry = CanonicalAutonomyRegistry()
