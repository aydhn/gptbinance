from typing import Dict, List, Optional
from .models import ObservabilityAuditRecord

class RuntimeTelemetryTracker:
    def __init__(self):
        self._audits: Dict[str, ObservabilityAuditRecord] = {}

    def report_audit(self, audit: ObservabilityAuditRecord) -> None:
        self._audits[audit.audit_id] = audit

    def get_audit(self, audit_id: str) -> Optional[ObservabilityAuditRecord]:
        return self._audits.get(audit_id)

    def list_audits(self) -> List[ObservabilityAuditRecord]:
        return list(self._audits.values())
