from typing import Dict, Any
from .models import EquitableSetoffRecord

class EquitableSetoffManager:
    def __init__(self):
        self.records: Dict[str, EquitableSetoffRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> EquitableSetoffRecord:
        rec = EquitableSetoffRecord(**data)
        self.records[rec.equitable_id] = rec
        return rec
