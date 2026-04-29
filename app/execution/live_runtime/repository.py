from app.execution.live_runtime.storage import LiveStorage
from app.execution.live_runtime.models import (
    LiveRun,
    LiveAccountSnapshot,
    LiveEquitySnapshot,
    LiveAuditRecord,
    LiveAfterActionSummary,
)
from typing import List, Optional


class LiveRepository:
    def __init__(self, storage: LiveStorage):
        self.storage = storage

    def save_run(self, run: LiveRun) -> None:
        self.storage.save_run(run)

    def get_run(self, run_id: str) -> Optional[LiveRun]:
        return self.storage.get_run(run_id)

    def save_account_snapshot(self, snapshot: LiveAccountSnapshot) -> None:
        self.storage.save_account_snapshot(snapshot.run_id, snapshot)

    def get_latest_account_snapshot(self, run_id: str) -> Optional[LiveAccountSnapshot]:
        return self.storage.get_latest_account_snapshot(run_id)

    def save_equity_snapshot(self, snapshot: LiveEquitySnapshot) -> None:
        self.storage.save_equity_snapshot(snapshot.run_id, snapshot)

    def get_latest_equity_snapshot(self, run_id: str) -> Optional[LiveEquitySnapshot]:
        return self.storage.get_latest_equity_snapshot(run_id)

    def save_audit_records(self, run_id: str, records: List[LiveAuditRecord]) -> None:
        self.storage.save_audit_records(run_id, records)

    def get_audit_records(self, run_id: str) -> List[LiveAuditRecord]:
        return self.storage.get_audit_records(run_id)

    def save_after_action_summary(self, summary: LiveAfterActionSummary) -> None:
        self.storage.save_after_action_summary(summary.run_id, summary)

    def get_after_action_summary(self, run_id: str) -> Optional[LiveAfterActionSummary]:
        return self.storage.get_after_action_summary(run_id)
