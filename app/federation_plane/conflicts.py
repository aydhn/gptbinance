from typing import Dict, List, Optional
from app.federation_plane.models import FederatedConflictRecord
from app.federation_plane.exceptions import FederationConflictViolation


class ConflictManager:
    def __init__(self):
        self._conflicts: Dict[str, FederatedConflictRecord] = {}

    def register(self, record: FederatedConflictRecord):
        if not record.conflict_id:
            raise FederationConflictViolation("No hidden contradiction allowed.")
        self._conflicts[record.conflict_id] = record

    def get_conflict(self, conflict_id: str) -> Optional[FederatedConflictRecord]:
        return self._conflicts.get(conflict_id)

    def list_conflicts(self) -> List[FederatedConflictRecord]:
        return list(self._conflicts.values())
