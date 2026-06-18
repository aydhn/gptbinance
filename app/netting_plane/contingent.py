from typing import Dict, Any
from .models import ContingentObligationRecord

class ContingentManager:
    def __init__(self):
        self.records: Dict[str, ContingentObligationRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> ContingentObligationRecord:
        rec = ContingentObligationRecord(**data)
        self.records[rec.contingent_id] = rec
        return rec
