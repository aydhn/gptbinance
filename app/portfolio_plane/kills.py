from typing import Dict, Optional
from app.portfolio_plane.models import KillRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class KillManager:
    def __init__(self):
        self._records: Dict[str, KillRecord] = {}

    def register(self, record: KillRecord):
        if record.kill_id in self._records:
            raise PortfolioStorageError(f"Kill {record.kill_id} already exists")
        if not record.evidence_notes:
            raise ValueError("Evidence notes are required for killing an initiative")
        self._records[record.kill_id] = record

    def get(self, record_id: str) -> Optional[KillRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, KillRecord]:
        return self._records.copy()
