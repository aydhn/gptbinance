from typing import Dict
from app.operating_model_plane.models import OperatingModelObject
from app.operating_model_plane.exceptions import OwnerlessCriticalSurfaceError

class CanonicalOperatingModelRegistry:
    def __init__(self):
        self._objects: Dict[str, OperatingModelObject] = {}

    def register(self, obj: OperatingModelObject):
        if obj.is_critical and obj.primary_owner is None:
            raise OwnerlessCriticalSurfaceError(f"Surface {obj.operating_id} is critical but lacks primary owner.")
        self._objects[obj.operating_id] = obj

    def get_object(self, operating_id: str) -> OperatingModelObject:
        return self._objects.get(operating_id)

    def get_all(self):
        return list(self._objects.values())
