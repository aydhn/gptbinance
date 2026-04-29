from app.execution.live_runtime.base import AuditWriterBase
from app.execution.live_runtime.models import (
    LiveAuditRecord,
    LiveAfterActionSummary,
    LiveSessionSummary,
)
from app.execution.live_runtime.enums import LiveAuditEventType
from typing import List
from datetime import datetime


class LiveAuditWriter(AuditWriterBase):
    def __init__(self):
        self.records: List[LiveAuditRecord] = []

    def write_record(self, record: LiveAuditRecord) -> None:
        self.records.append(record)
        # In a real app, this would append to a file/DB immediately

    def get_records(self) -> List[LiveAuditRecord]:
        return self.records

    def generate_after_action_summary(
        self, run_id: str, summary: LiveSessionSummary
    ) -> LiveAfterActionSummary:
        return LiveAfterActionSummary(
            run_id=run_id,
            summary=summary,
            key_events=self.records,
            generated_at=datetime.utcnow(),
        )
