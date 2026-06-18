from typing import Dict, Any
from .models import StayedObligationRecord

class StayedManager:
    def __init__(self):
        self.records: Dict[str, StayedObligationRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> StayedObligationRecord:
        rec = StayedObligationRecord(**data)
        self.records[rec.stayed_id] = rec
        return rec
