from typing import Dict, Any
from .models import CounterpartyCapacityRecord

class CapacityManager:
    def __init__(self):
        self.capacities: Dict[str, CounterpartyCapacityRecord] = {}

    def register_capacity(self, data: Dict[str, Any]) -> CounterpartyCapacityRecord:
        cap = CounterpartyCapacityRecord(**data)
        self.capacities[cap.capacity_id] = cap
        return cap
