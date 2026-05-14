from typing import Dict, List, Optional
from app.value_plane.models import ValueDivergenceReport

class DivergenceRegistry:
    def __init__(self):
        self._records: Dict[str, ValueDivergenceReport] = {}

    def register(self, record: ValueDivergenceReport):
        self._records[record.report_id] = record

    def get(self, record_id: str) -> Optional[ValueDivergenceReport]:
        return self._records.get(record_id)

    def list_all(self) -> List[ValueDivergenceReport]:
        return list(self._records.values())

divergence_registry = DivergenceRegistry()
