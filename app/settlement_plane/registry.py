from typing import Dict
from app.settlement_plane.base import BaseSettlementRegistry
from app.settlement_plane.models import SettlementObject

class CanonicalSettlementRegistry(BaseSettlementRegistry):
    def __init__(self):
        self._objects: Dict[str, SettlementObject] = {}

    def register_settlement(self, obj: SettlementObject) -> str:
        if obj.id in self._objects:
            raise ValueError(f"SettlementObject {obj.id} already exists")
        self._objects[obj.id] = obj
        return obj.id

    def get_settlement(self, obj_id: str) -> SettlementObject:
        if obj_id not in self._objects:
            raise KeyError(f"SettlementObject {obj_id} not found")
        return self._objects[obj_id]
