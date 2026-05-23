from typing import Dict, List, Optional
from app.interpretation_plane.models import InterpretationObject
from app.interpretation_plane.exceptions import InvalidInterpretationObject

class CanonicalInterpretationRegistry:
    def __init__(self):
        self._objects: Dict[str, InterpretationObject] = {}

    def register(self, obj: InterpretationObject):
        if not obj.interpretation_id:
            raise InvalidInterpretationObject("Missing interpretation ID.")
        self._objects[obj.interpretation_id] = obj

    def get(self, interpretation_id: str) -> Optional[InterpretationObject]:
        return self._objects.get(interpretation_id)

    def get_all(self) -> List[InterpretationObject]:
        return list(self._objects.values())
