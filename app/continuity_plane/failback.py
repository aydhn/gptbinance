from typing import Dict, List, Optional
from app.continuity_plane.models import FailbackRecord
from app.continuity_plane.exceptions import FailbackViolation

class FailbackManager:
    def __init__(self):
        self._failbacks: Dict[str, FailbackRecord] = {}

    def record_failback(self, record: FailbackRecord) -> None:
        self._failbacks[record.failback_id] = record

    def get_failback(self, failback_id: str) -> Optional[FailbackRecord]:
        return self._failbacks.get(failback_id)

    def list_failbacks(self) -> List[FailbackRecord]:
        return list(self._failbacks.values())
