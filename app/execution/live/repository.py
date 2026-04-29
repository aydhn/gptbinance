from typing import Dict, Any, List
from app.execution.live.storage import ExecutionStorage
from app.execution.live.models import ExecutionAuditRecord, ExecutionRun


class ExecutionRepository:
    def __init__(self, storage: ExecutionStorage):
        self.storage = storage

    def start_run(self, run: ExecutionRun):
        self.storage.save_snapshot(run.run_id, "run_info", run.dict())

    def append_audit(self, record: ExecutionAuditRecord):
        self.storage.save_audit_record(record.run_id, record.dict())
