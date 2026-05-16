from typing import Dict, Optional
from app.portfolio_plane.models import StrategicFitRecord
from app.portfolio_plane.exceptions import PortfolioStorageError

class StrategicFitManager:
    def __init__(self):
        self._records: Dict[str, StrategicFitRecord] = {}

    def register(self, record: StrategicFitRecord):
        if record.fit_id in self._records:
            raise PortfolioStorageError(f"StrategicFit {record.fit_id} already exists")
        if not record.proof_notes:
            raise ValueError("Proof notes are required for strategic fit")
        self._records[record.fit_id] = record

    def get(self, record_id: str) -> Optional[StrategicFitRecord]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, StrategicFitRecord]:
        return self._records.copy()
