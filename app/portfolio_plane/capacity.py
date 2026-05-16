from typing import Dict, Optional
from app.portfolio_plane.models import CapacityReservationRef
from app.portfolio_plane.exceptions import PortfolioStorageError

class CapacityManager:
    def __init__(self):
        self._records: Dict[str, CapacityReservationRef] = {}

    def register(self, record: CapacityReservationRef):
        if record.reservation_id in self._records:
            raise PortfolioStorageError(f"Reservation {record.reservation_id} already exists")
        if record.capacity_allocated < 0:
            raise ValueError("Capacity cannot be negative.")
        self._records[record.reservation_id] = record

    def get(self, record_id: str) -> Optional[CapacityReservationRef]:
        return self._records.get(record_id)

    def get_all(self) -> Dict[str, CapacityReservationRef]:
        return self._records.copy()
