from typing import Dict, Any
from .models import PartialNettingRecord

class PartialsManager:
    def __init__(self):
        self.records: Dict[str, PartialNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> PartialNettingRecord:
        rec = PartialNettingRecord(**data)
        self.records[rec.partial_id] = rec
        return rec
