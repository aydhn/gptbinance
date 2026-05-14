from typing import Dict, List, Optional
from app.value_plane.models import RiskAdjustedValueRecord

class RiskAdjustedRegistry:
    def __init__(self):
        self._records: Dict[str, RiskAdjustedValueRecord] = {}

    def register(self, record: RiskAdjustedValueRecord):
        self._records[record.record_id] = record

    def get(self, record_id: str) -> Optional[RiskAdjustedValueRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[RiskAdjustedValueRecord]:
        return list(self._records.values())

risk_adjusted_registry = RiskAdjustedRegistry()
