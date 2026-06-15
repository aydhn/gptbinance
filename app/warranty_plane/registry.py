from typing import Dict, List
from app.warranty_plane.models import WarrantyObject
from app.warranty_plane.enums import WarrantyClass

class CanonicalWarrantyRegistry:
    def __init__(self):
        self._objects: Dict[str, WarrantyObject] = {}

    def register_warranty(self, warranty_id: str, owner: str, class_type: WarrantyClass, scope: str) -> WarrantyObject:
        obj = WarrantyObject(warranty_id=warranty_id, owner=owner, class_type=class_type, scope=scope)
        self._objects[warranty_id] = obj
        return obj

    def get_warranty(self, warranty_id: str) -> WarrantyObject:
        return self._objects.get(warranty_id)

    def list_warranties(self) -> List[WarrantyObject]:
        return list(self._objects.values())
