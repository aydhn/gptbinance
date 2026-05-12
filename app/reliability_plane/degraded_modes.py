from datetime import datetime
from typing import Dict, List, Optional

from .exceptions import DegradedModeViolation
from .models import DegradedModeRecord


class DegradedModeManager:
    def __init__(self):
        self._records: Dict[str, List[DegradedModeRecord]] = {}

    def record_degraded_mode(self, record: DegradedModeRecord) -> None:
        if record.service_id not in self._records:
            self._records[record.service_id] = []
        self._records[record.service_id].append(record)

    def get_active_degraded_modes(self, service_id: str) -> List[DegradedModeRecord]:
        # Simplification: assume all records not explicitly closed or mapped to exit are active.
        # In a real system, you'd check if it was exited.
        # For now, return all that aren't marked with some end condition (which we haven't strictly modeled yet).
        return self._records.get(service_id, [])

    def list_all_degraded_modes(self) -> List[DegradedModeRecord]:
        result = []
        for records in self._records.values():
            result.extend(records)
        return result

    def check_for_overdue(
        self, service_id: str, current_time: datetime, max_duration_hours: int = 24
    ) -> None:
        records = self.get_active_degraded_modes(service_id)
        for r in records:
            if (
                current_time - r.start_time
            ).total_seconds() > max_duration_hours * 3600:
                r.is_overdue = True
