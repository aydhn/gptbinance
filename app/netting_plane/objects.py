from typing import Dict, Any
from .models import NettingObject, NettingObjectRef

class NettingObjectManager:
    def __init__(self):
        self.objects: Dict[str, NettingObject] = {}

    def create_object(self, data: Dict[str, Any]) -> NettingObject:
        obj = NettingObject(**data)
        self.objects[obj.netting_id] = obj
        return obj

    def get_object(self, netting_id: str) -> NettingObject:
        return self.objects.get(netting_id)
