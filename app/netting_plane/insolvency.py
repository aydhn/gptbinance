from typing import Dict, Any
from .models import InsolvencySafeNettingRecord

class InsolvencyManager:
    def __init__(self):
        self.records: Dict[str, InsolvencySafeNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> InsolvencySafeNettingRecord:
        rec = InsolvencySafeNettingRecord(**data)
        self.records[rec.insolvency_id] = rec
        return rec
