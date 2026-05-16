from typing import Dict, Optional
from app.portfolio_plane.models import DeferralRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class DeferralManager:
    def __init__(self):
        self._records: Dict[str, DeferralRecord] = {}

    def register(self, record: DeferralRecord):
        if record.deferral_id in self._records:
            raise PortfolioStorageError(f"Deferral {record.deferral_id} already exists")
        if not record.deferral_reason:
            raise ValueError("Reason is required for deferral")
        self._records[record.deferral_id] = record

    def get(self, record_id: str) -> Optional[DeferralRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, DeferralRecord]:
        return self._records.copy()
