from typing import Dict, Optional
from app.portfolio_plane.models import FreezeRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class FreezeManager:
    def __init__(self):
        self._records: Dict[str, FreezeRecord] = {}

    def register(self, record: FreezeRecord):
        if record.freeze_id in self._records:
            raise PortfolioStorageError(f"Freeze {record.freeze_id} already exists")
        if not record.rationale:
            raise ValueError("Rationale is required for freeze")
        self._records[record.freeze_id] = record

    def get(self, record_id: str) -> Optional[FreezeRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, FreezeRecord]:
        return self._records.copy()
