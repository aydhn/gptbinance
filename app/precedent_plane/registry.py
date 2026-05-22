from app.precedent_plane.models import PrecedentObject
from app.precedent_plane.exceptions import InvalidPrecedentObjectError
from typing import Dict, List

class CanonicalPrecedentRegistry:
    def __init__(self):
        self._precedents: Dict[str, PrecedentObject] = {}

    def register(self, obj: PrecedentObject):
        if not obj.precedent_id:
            raise InvalidPrecedentObjectError("Undocumented precedent id")
        self._precedents[obj.precedent_id] = obj

    def get(self, precedent_id: str) -> PrecedentObject:
        return self._precedents.get(precedent_id)

    def list_all(self) -> List[PrecedentObject]:
        return list(self._precedents.values())
