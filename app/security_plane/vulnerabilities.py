from typing import Dict, List, Optional
from app.security_plane.models import VulnerabilityRecord

class VulnerabilityRegistry:
    def __init__(self):
        self._vulns: Dict[str, VulnerabilityRecord] = {}

    def register_vulnerability(self, vuln: VulnerabilityRecord) -> None:
        self._vulns[vuln.vuln_id] = vuln

    def list_vulnerabilities(self) -> List[VulnerabilityRecord]:
        return list(self._vulns.values())
