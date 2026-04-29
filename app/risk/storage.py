from typing import List, Dict, Any
from app.risk.models import RiskAuditRecord


class RiskStorage:
    def __init__(self):
        self.records: List[RiskAuditRecord] = []

    def save_audit(self, record: RiskAuditRecord):
        self.records.append(record)
        # In a real system, insert to DB/Parquet

    def get_by_run(self, run_id: str) -> List[RiskAuditRecord]:
        return [r for r in self.records if r.run_id == run_id]
