from typing import Dict, Any
from .models import DisputedObligationRecord

class DisputedManager:
    def __init__(self):
        self.records: Dict[str, DisputedObligationRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> DisputedObligationRecord:
        rec = DisputedObligationRecord(**data)
        self.records[rec.disputed_id] = rec
        return rec
