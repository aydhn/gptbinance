from typing import Dict, Optional
from app.portfolio_plane.models import StageFundingRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class StageFundingManager:
    def __init__(self):
        self._records: Dict[str, StageFundingRecord] = {}

    def register(self, record: StageFundingRecord):
        if record.stage_funding_id in self._records:
            raise PortfolioStorageError(f"StageFunding {record.stage_funding_id} already exists")
        if not record.gate_evidence:
            raise ValueError("Gate evidence is required for stage funding")
        self._records[record.stage_funding_id] = record

    def get(self, record_id: str) -> Optional[StageFundingRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, StageFundingRecord]:
        return self._records.copy()
