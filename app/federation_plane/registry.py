from typing import Dict, List, Optional
from app.federation_plane.models import FederationRecord, FederationObject
from app.federation_plane.exceptions import FederationStorageError


class CanonicalFederationRegistry:
    def __init__(self):
        self._federations: Dict[str, FederationRecord] = {}
        self._objects: Dict[str, FederationObject] = {}

    def register_federation(self, federation: FederationRecord):
        if not federation.federation_id:
            raise FederationStorageError("Undocumented federation ID.")
        self._federations[federation.federation_id] = federation

    def get_federation(self, federation_id: str) -> Optional[FederationRecord]:
        return self._federations.get(federation_id)

    def register_object(self, obj: FederationObject):
        if not obj.federation_id:
            raise FederationStorageError("Undocumented federation object ID.")
        self._objects[obj.federation_id] = obj

    def list_federations(self) -> List[FederationRecord]:
        return list(self._federations.values())
