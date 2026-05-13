from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityStateSnapshot

class ContinuityStateManager:
    def __init__(self):
        self._states: Dict[str, ContinuityStateSnapshot] = {}

    def update_state(self, record: ContinuityStateSnapshot) -> None:
        self._states[record.service_id] = record

    def get_state(self, service_id: str) -> Optional[ContinuityStateSnapshot]:
        return self._states.get(service_id)

    def list_states(self) -> List[ContinuityStateSnapshot]:
        return list(self._states.values())
