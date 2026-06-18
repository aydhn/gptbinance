from typing import Dict, Any
from .models import CloseoutNettingRecord

class CloseoutNettingManager:
    def __init__(self):
        self.records: Dict[str, CloseoutNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> CloseoutNettingRecord:
        rec = CloseoutNettingRecord(**data)
        self.records[rec.closeout_netting_id] = rec
        return rec
