from typing import Dict, Optional
from app.portfolio_plane.models import FundingRecord
from app.portfolio_plane.exceptions import InvalidFundingRecordError, PortfolioStorageError

class FundingManager:
    def __init__(self):
        self._records: Dict[str, FundingRecord] = {}

    def register(self, record: FundingRecord):
        if record.funding_id in self._records:
            raise PortfolioStorageError(f"Funding {record.funding_id} already exists")
        if record.envelope_allocated < 0:
            raise InvalidFundingRecordError("Envelope cannot be negative.")
        self._records[record.funding_id] = record

    def get(self, record_id: str) -> Optional[FundingRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, FundingRecord]:
        return self._records.copy()
