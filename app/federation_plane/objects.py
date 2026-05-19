from typing import Dict, Optional
from app.federation_plane.models import FederationObject


class FederationObjectManager:
    def __init__(self):
        self._objects: Dict[str, FederationObject] = {}

    def register(self, obj: FederationObject):
        self._objects[obj.federation_id] = obj

    def get_object(self, federation_id: str) -> Optional[FederationObject]:
        return self._objects.get(federation_id)
