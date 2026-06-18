from typing import Dict, Any
from .models import SetoffReversalRecord

class ReversalManager:
    def __init__(self):
        self.records: Dict[str, SetoffReversalRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> SetoffReversalRecord:
        rec = SetoffReversalRecord(**data)
        self.records[rec.reversal_id] = rec
        return rec
