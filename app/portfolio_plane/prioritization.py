from typing import Dict, Optional
from app.portfolio_plane.models import PrioritizationRecord
from app.portfolio_plane.exceptions import InvalidPrioritizationRecordError, PortfolioStorageError

class PrioritizationManager:
    def __init__(self):
        self._records: Dict[str, PrioritizationRecord] = {}

    def register(self, record: PrioritizationRecord):
        if record.prioritization_id in self._records:
            raise PortfolioStorageError(f"Prioritization {record.prioritization_id} already exists")
        if not record.proof_notes:
            raise InvalidPrioritizationRecordError("Proof notes are required for prioritization.")
        self._records[record.prioritization_id] = record

    def get(self, record_id: str) -> Optional[PrioritizationRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, PrioritizationRecord]:
        return self._records.copy()
