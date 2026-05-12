from typing import Dict, List, Optional
from .exceptions import ObservabilityPlaneError

class QualityAnalyzer:
    def __init__(self):
        self._quality_findings: Dict[str, List[str]] = {}

    def report_finding(self, telemetry_id: str, finding: str) -> None:
        if telemetry_id not in self._quality_findings:
            self._quality_findings[telemetry_id] = []
        self._quality_findings[telemetry_id].append(finding)

    def get_findings(self, telemetry_id: str) -> List[str]:
        return self._quality_findings.get(telemetry_id, [])

    def list_findings(self) -> Dict[str, List[str]]:
        return self._quality_findings.copy()
