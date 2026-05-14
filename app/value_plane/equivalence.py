from typing import Dict, List, Optional
from app.value_plane.models import ValueEquivalenceReport

class EquivalenceRegistry:
    def __init__(self):
        self._records: Dict[str, ValueEquivalenceReport] = {}

    def register(self, record: ValueEquivalenceReport):
        self._records[record.report_id] = record

    def get(self, record_id: str) -> Optional[ValueEquivalenceReport]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueEquivalenceReport]:
        return list(self._records.values())

equivalence_registry = EquivalenceRegistry()
