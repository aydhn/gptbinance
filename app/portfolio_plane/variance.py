from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioVarianceRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class VarianceManager:
    def __init__(self):
        self._records: Dict[str, PortfolioVarianceRecord] = {}

    def register(self, record: PortfolioVarianceRecord):
        if record.variance_id in self._records:
            raise PortfolioStorageError(f"Variance {record.variance_id} already exists")
        if not record.proof_notes:
            raise ValueError("Proof notes are required for variance")
        self._records[record.variance_id] = record

    def get(self, record_id: str) -> Optional[PortfolioVarianceRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, PortfolioVarianceRecord]:
        return self._records.copy()
