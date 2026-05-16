from typing import Dict, Optional
from app.portfolio_plane.models import StaffingRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class StaffingManager:
    def __init__(self):
        self._records: Dict[str, StaffingRecord] = {}

    def register(self, record: StaffingRecord):
        if record.staffing_id in self._records:
            raise PortfolioStorageError(f"Staffing {record.staffing_id} already exists")
        if not record.assigned_team:
            raise ValueError("Assigned team must be specified.")
        self._records[record.staffing_id] = record

    def get(self, record_id: str) -> Optional[StaffingRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, StaffingRecord]:
        return self._records.copy()
