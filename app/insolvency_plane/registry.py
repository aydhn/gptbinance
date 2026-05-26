from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyObject
from app.insolvency_plane.enums import InsolvencyClass
from app.insolvency_plane.exceptions import InvalidInsolvencyObjectError

class InsolvencyRegistry:
    def __init__(self):
        self._objects: Dict[str, InsolvencyObject] = {}

    def register(self, obj: InsolvencyObject):
        if not obj.id or not obj.class_type:
            raise InvalidInsolvencyObjectError("Insolvency object must have ID and class_type")
        self._objects[obj.id] = obj

    def get(self, obj_id: str) -> Optional[InsolvencyObject]:
        return self._objects.get(obj_id)

    def list_all(self) -> List[InsolvencyObject]:
        return list(self._objects.values())

    def get_by_class(self, class_type: InsolvencyClass) -> List[InsolvencyObject]:
        return [obj for obj in self._objects.values() if obj.class_type == class_type]
