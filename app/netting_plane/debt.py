from typing import Dict, Any
from .models import NettingDebtRecord

class DebtManager:
    def __init__(self):
        self.records: Dict[str, NettingDebtRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> NettingDebtRecord:
        rec = NettingDebtRecord(**data)
        self.records[rec.debt_id] = rec
        return rec
