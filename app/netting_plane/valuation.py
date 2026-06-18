from typing import Dict, Any
from .models import ValuationRecord

class ValuationManager:
    def __init__(self):
        self.records: Dict[str, ValuationRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> ValuationRecord:
        rec = ValuationRecord(**data)
        self.records[rec.valuation_id] = rec
        return rec
