from typing import Dict, List, Optional
from app.value_plane.models import RealizedImpactRecord
from app.value_plane.exceptions import ValuePlaneError

class RealizedImpactRegistry:
    def __init__(self):
        self._records: Dict[str, RealizedImpactRecord] = {}

    def register(self, record: RealizedImpactRecord):
        if not record.baseline_ref:
            raise ValuePlaneError("No baseline-free impact claim allowed. Must provide a baseline_ref.")
        self._records[record.realized_impact_id] = record

    def get(self, record_id: str) -> Optional[RealizedImpactRecord]:
        return self._records.get(record_id)

    def list_all(self) -> List[RealizedImpactRecord]:
        return list(self._records.values())

realized_impact_registry = RealizedImpactRegistry()
