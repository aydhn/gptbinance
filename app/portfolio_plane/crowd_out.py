from typing import Dict, Optional
from app.portfolio_plane.models import CrowdOutRecord
from app.portfolio_plane.exceptions import CrowdOutViolationError, PortfolioStorageError

class CrowdOutManager:
    def __init__(self):
        self._records: Dict[str, CrowdOutRecord] = {}

    def register(self, record: CrowdOutRecord):
        if record.crowd_out_id in self._records:
            raise PortfolioStorageError(f"CrowdOut {record.crowd_out_id} already exists")
        if not record.rationale:
            raise CrowdOutViolationError("Rationale is required for crowd-out.")
        if record.displacing_portfolio_id == record.displaced_portfolio_id:
             raise CrowdOutViolationError("A portfolio cannot displace itself.")
        self._records[record.crowd_out_id] = record

    def get(self, record_id: str) -> Optional[CrowdOutRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, CrowdOutRecord]:
        return self._records.copy()
