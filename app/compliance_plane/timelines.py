from app.compliance_plane.models import ComplianceAuditRecord
from typing import List


class TimelineManager:
    def __init__(self):
        self._records: List[ComplianceAuditRecord] = []

    def add_record(self, record: ComplianceAuditRecord) -> None:
        self._records.append(record)

    def get_timeline(self) -> List[ComplianceAuditRecord]:
        return sorted(self._records, key=lambda x: x.timestamp)
