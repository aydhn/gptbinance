from typing import Dict, List, Optional
from app.value_plane.models import ValueObject
from app.value_plane.exceptions import InvalidValueObject

class ValueRegistry:
    def __init__(self):
        self._objects: Dict[str, ValueObject] = {}

    def register(self, value_object: ValueObject):
        if not value_object.value_id:
            raise InvalidValueObject("Value object must have a valid value_id")
        self._objects[value_object.value_id] = value_object

    def get(self, value_id: str) -> Optional[ValueObject]:
        return self._objects.get(value_id)

    def list_all(self) -> List[ValueObject]:
        return list(self._objects.values())

value_registry = ValueRegistry()
