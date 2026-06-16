from app.indemnity_plane.models import IndemnityObject
from app.indemnity_plane.exceptions import IndemnityStorageError

class CanonicalIndemnityRegistry:
    def __init__(self):
        self._indemnities = {}

    def register(self, obj: IndemnityObject):
        self._indemnities[obj.id] = obj

    def get(self, indemnity_id: str) -> IndemnityObject:
        return self._indemnities.get(indemnity_id)

    def list_all(self):
        return list(self._indemnities.values())
