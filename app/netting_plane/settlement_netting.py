from typing import Dict, Any
from .models import SettlementNettingRecord

class SettlementNettingManager:
    def __init__(self):
        self.records: Dict[str, SettlementNettingRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> SettlementNettingRecord:
        rec = SettlementNettingRecord(**data)
        self.records[rec.settlement_netting_id] = rec
        return rec
