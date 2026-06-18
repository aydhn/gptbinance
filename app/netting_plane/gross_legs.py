from typing import Dict, Any
from .models import GrossLegAuditRecord

class GrossLegsManager:
    def __init__(self):
        self.records: Dict[str, GrossLegAuditRecord] = {}

    def evaluate(self, data: Dict[str, Any]) -> GrossLegAuditRecord:
        rec = GrossLegAuditRecord(**data)
        self.records[rec.gross_leg_id] = rec
        return rec
