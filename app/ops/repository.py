from app.ops.storage import OpsStorage
from app.ops.models import (
    OpsRun,
    ReadinessReport,
    OpsAuditRecord,
    IncidentRecord,
    MaintenanceWindow,
    GoLiveGateReport,
    RecoveryResult,
)
from typing import List, Optional


class OpsRepository:
    def __init__(self, storage: OpsStorage):
        self.storage = storage

    def save_run(self, run: OpsRun) -> None:
        self.storage.save_record(run.run_id, "run", run.model_dump())

    def get_run(self, run_id: str) -> Optional[OpsRun]:
        data = self.storage.load_record(run_id, "run")
        return OpsRun(**data) if data else None

    def save_readiness_report(self, report: ReadinessReport) -> None:
        self.storage.save_record(report.run_id, "readiness", report.model_dump())

    def get_readiness_report(self, run_id: str) -> Optional[ReadinessReport]:
        data = self.storage.load_record(run_id, "readiness")
        return ReadinessReport(**data) if data else None

    def append_audit_record(self, record: OpsAuditRecord) -> None:
        self.storage.append_record(record.run_id, "audit", record.model_dump())

    def get_audit_records(self, run_id: str) -> List[OpsAuditRecord]:
        data = self.storage.load_records(run_id, "audit") or []
        return [OpsAuditRecord(**r) for r in data]

    def append_incident(self, incident: IncidentRecord) -> None:
        self.storage.append_record(incident.run_id, "incidents", incident.model_dump())

    def get_incidents(self, run_id: str) -> List[IncidentRecord]:
        data = self.storage.load_records(run_id, "incidents") or []
        return [IncidentRecord(**r) for r in data]

    def save_maintenance_window(self, window: MaintenanceWindow) -> None:
        self.storage.append_record("global", "maintenance", window.model_dump())

    def get_maintenance_windows(self) -> List[MaintenanceWindow]:
        data = self.storage.load_records("global", "maintenance") or []
        return [MaintenanceWindow(**r) for r in data]

    def save_go_live_report(self, run_id: str, report: GoLiveGateReport) -> None:
        self.storage.save_record(run_id, "go_live", report.model_dump())

    def save_recovery_result(self, result: RecoveryResult) -> None:
        self.storage.save_record(result.run_id, "recovery", result.model_dump())

    def get_recovery_result(self, run_id: str) -> Optional[RecoveryResult]:
        data = self.storage.load_record(run_id, "recovery")
        return RecoveryResult(**data) if data else None
