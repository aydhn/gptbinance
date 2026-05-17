from typing import List, Dict
from app.change_plane.models import ChangeObject
from app.change_plane.base import ChangeRegistryBase
from app.change_plane.exceptions import InvalidChangeObjectError

class CanonicalChangeRegistry(ChangeRegistryBase):
    def __init__(self):
        self._changes: Dict[str, ChangeObject] = {}

    def register(self, change: ChangeObject):
        if not change.change_id:
            raise InvalidChangeObjectError("No vague change names or undocumented ids")
        self._changes[change.change_id] = change

    def get_change(self, change_id: str) -> ChangeObject:
        return self._changes.get(change_id)

    def get_all(self) -> List[ChangeObject]:
        return list(self._changes.values())
