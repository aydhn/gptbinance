from datetime import datetime
from typing import Dict, List, Optional

from .exceptions import MaintenanceViolation
from .models import MaintenanceWindowRecord


class MaintenanceManager:
    def __init__(self):
        self._records: Dict[str, List[MaintenanceWindowRecord]] = {}

    def schedule_maintenance(self, record: MaintenanceWindowRecord) -> None:
        if not record.approvals and record.maintenance_class.value == "planned":
            raise MaintenanceViolation("Planned maintenance requires approvals.")
        if record.service_id not in self._records:
            self._records[record.service_id] = []
        self._records[record.service_id].append(record)

    def get_maintenance_windows(self, service_id: str) -> List[MaintenanceWindowRecord]:
        return self._records.get(service_id, [])

    def list_all_maintenance_windows(self) -> List[MaintenanceWindowRecord]:
        result = []
        for records in self._records.values():
            result.extend(records)
        return result

    def check_masking(self, service_id: str, current_time: datetime) -> bool:
        # Simplistic check if multiple emergency maintenances exist recently
        # In real life, compare to error budgets or actual outages
        records = self.get_maintenance_windows(service_id)
        emergency_count = sum(
            1 for r in records if r.maintenance_class.value == "emergency"
        )
        return emergency_count > 3
