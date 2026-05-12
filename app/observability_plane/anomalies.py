from typing import Dict, List, Optional
from .models import TelemetryAnomalyFinding

class AnomalyDetectorRegistry:
    def __init__(self):
        self._findings: Dict[str, TelemetryAnomalyFinding] = {}

    def report_anomaly(self, finding: TelemetryAnomalyFinding) -> None:
        self._findings[finding.anomaly_id] = finding

    def get_anomaly(self, anomaly_id: str) -> Optional[TelemetryAnomalyFinding]:
        return self._findings.get(anomaly_id)

    def list_anomalies(self) -> List[TelemetryAnomalyFinding]:
        return list(self._findings.values())
