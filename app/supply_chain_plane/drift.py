from typing import Dict, Optional, List
from app.supply_chain_plane.models import DriftRecord


class DriftRegistry:
    def __init__(self):
        self._records: Dict[str, DriftRecord] = {}

    def register_drift(self, drift: DriftRecord) -> None:
        self._records[drift.drift_id] = drift

    def get_drift(self, drift_id: str) -> Optional[DriftRecord]:
        return self._records.get(drift_id)

    def get_drifts_for_component(self, component_id: str) -> List[DriftRecord]:
        return [
            d
            for d in self._records.values()
            if d.component_ref.component_id == component_id
        ]
