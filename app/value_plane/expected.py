from typing import Dict, List, Optional
from app.value_plane.models import ExpectedImpactRecord

class ExpectedImpactRegistry:
    def __init__(self):
        self._records: Dict[str, ExpectedImpactRecord] = {}

    def register(self, record: ExpectedImpactRecord):
        self._records[record.expected_impact_id] = record

    def get(self, record_id: str) -> Optional[ExpectedImpactRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[ExpectedImpactRecord]:
        return list(self._records.values())

expected_impact_registry = ExpectedImpactRegistry()
