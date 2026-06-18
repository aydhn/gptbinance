from typing import Dict, Any
from .models import NovationNettingRecord

class NovationManager:
    def __init__(self):
        self.records: Dict[str, NovationNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> NovationNettingRecord:
        rec = NovationNettingRecord(**data)
        self.records[rec.novation_id] = rec
        return rec
