from typing import Dict, Optional
from app.portfolio_plane.models import SequencingRecord
from app.portfolio_plane.exceptions import SequencingViolationError, PortfolioStorageError

class SequencingManager:
    def __init__(self):
        self._records: Dict[str, SequencingRecord] = {}

    def register(self, record: SequencingRecord):
        if record.sequencing_id in self._records:
            raise PortfolioStorageError(f"Sequencing {record.sequencing_id} already exists")
        if not record.rationale_notes:
            raise SequencingViolationError("Rationale notes are required for sequencing.")
        self._records[record.sequencing_id] = record

    def get(self, record_id: str) -> Optional[SequencingRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, SequencingRecord]:
        return self._records.copy()
