from app.compliance_plane.models import ComplianceRecurrenceRecord
from typing import Dict, List


class RecurrenceManager:
    def __init__(self):
        self._records: Dict[str, ComplianceRecurrenceRecord] = {}

    def register_recurrence(self, rec: ComplianceRecurrenceRecord) -> None:
        self._records[rec.recurrence_id] = rec

    def list_recurrences(self) -> List[ComplianceRecurrenceRecord]:
        return list(self._records.values())
