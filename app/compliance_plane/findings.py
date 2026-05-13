from app.compliance_plane.models import AuditFinding
from typing import Dict, List


class FindingManager:
    def __init__(self):
        self._findings: Dict[str, AuditFinding] = {}

    def register_finding(self, finding: AuditFinding) -> None:
        self._findings[finding.finding_id] = finding

    def list_findings(self) -> List[AuditFinding]:
        return list(self._findings.values())

class StaleSecretRotationFinding(AuditFinding):
    pass

class ExpiredCertFinding(AuditFinding):
    pass

class OrphanTokenFinding(AuditFinding):
    pass

class MissingPatchVerificationFinding(AuditFinding):
    pass

class BoundaryAmbiguityFinding(AuditFinding):
    pass
