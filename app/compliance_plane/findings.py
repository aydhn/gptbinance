from app.compliance_plane.models import AuditFinding
from typing import Dict, List


class FindingManager:
    def __init__(self):
        self._findings: Dict[str, AuditFinding] = {}

    def register_finding(self, finding: AuditFinding) -> None:
        self._findings[finding.finding_id] = finding

    def list_findings(self) -> List[AuditFinding]:
        return list(self._findings.values())
