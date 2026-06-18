from typing import Dict, Any
from .models import DuePayableRecord

class DuePayableManager:
    def __init__(self):
        self.records: Dict[str, DuePayableRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> DuePayableRecord:
        rec = DuePayableRecord(**data)
        self.records[rec.due_id] = rec
        return rec
