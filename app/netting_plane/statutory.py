from typing import Dict, Any
from .models import StatutorySetoffRecord

class StatutorySetoffManager:
    def __init__(self):
        self.records: Dict[str, StatutorySetoffRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> StatutorySetoffRecord:
        rec = StatutorySetoffRecord(**data)
        self.records[rec.statutory_id] = rec
        return rec
