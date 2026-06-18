from typing import Dict, Any, List
from .base import NettingRegistryBase
from .models import NettingObject
from .enums import NettingClass

class CanonicalNettingRegistry(NettingRegistryBase):
    def __init__(self):
        self.records: Dict[str, NettingObject] = {}

    def register(self, netting_id: str, data: Dict[str, Any]) -> None:
        obj = NettingObject(**data)
        self.records[netting_id] = obj

    def get(self, netting_id: str) -> Dict[str, Any]:
        obj = self.records.get(netting_id)
        return obj.model_dump() if obj else {}

    def list_by_class(self, class_name: NettingClass) -> List[Dict[str, Any]]:
        return [obj.model_dump() for obj in self.records.values() if obj.class_name == class_name]
