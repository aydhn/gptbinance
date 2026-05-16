from typing import Dict, Optional
from app.portfolio_plane.models import CommitmentRecord
from app.portfolio_plane.exceptions import InvalidCommitmentRecordError, PortfolioStorageError

class CommitmentManager:
    def __init__(self):
        self._records: Dict[str, CommitmentRecord] = {}

    def register(self, record: CommitmentRecord):
        if record.commitment_id in self._records:
            raise PortfolioStorageError(f"Commitment {record.commitment_id} already exists")
        self._records[record.commitment_id] = record

    def get(self, record_id: str) -> Optional[CommitmentRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, CommitmentRecord]:
        return self._records.copy()
