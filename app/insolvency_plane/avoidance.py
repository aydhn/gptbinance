# avoidance.py
from typing import Dict, List, Optional
from pydantic import BaseModel

class AvoidanceRecord(BaseModel):
    avoidance_id: str
    transfer_description: str
    avoidance_type: str # preference, insider, fraudulent
    status: str
    lineage_refs: List[str]

class AvoidanceManager:
    def __init__(self):
        self.avoidances: Dict[str, AvoidanceRecord] = {}

    def register_avoidance(self, avoidance: AvoidanceRecord):
        self.avoidances[avoidance.avoidance_id] = avoidance

    def get_avoidance(self, avoidance_id: str) -> Optional[AvoidanceRecord]:
        return self.avoidances.get(avoidance_id)

    def list_avoidances(self) -> List[AvoidanceRecord]:
        return list(self.avoidances.values())
