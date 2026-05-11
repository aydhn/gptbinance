from app.compliance_plane.models import ComplianceRemediation
from typing import Dict, List
from datetime import datetime, timezone


class RemediationManager:
    def __init__(self):
        self._remediations: Dict[str, ComplianceRemediation] = {}

    def register_remediation(self, remediation: ComplianceRemediation) -> None:
        self._remediations[remediation.remediation_id] = remediation

    def update_overdue_states(self) -> None:
        now = datetime.now(timezone.utc)
        for r in self._remediations.values():
            if now > r.due_at:
                r.is_overdue = True

    def list_remediations(self) -> List[ComplianceRemediation]:
        return list(self._remediations.values())
