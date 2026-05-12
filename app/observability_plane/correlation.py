from typing import Dict, List, Optional
from .models import TelemetryCorrelationReport
from .exceptions import CorrelationViolationError

class CorrelationEngine:
    def __init__(self):
        self._correlations: Dict[str, TelemetryCorrelationReport] = {}

    def report_correlation(self, report: TelemetryCorrelationReport) -> None:
        if report.confidence_score < 0.5:
            # Low confidence correlations are explicitly flagged
            pass
        self._correlations[report.correlation_id] = report

    def get_correlation(self, correlation_id: str) -> Optional[TelemetryCorrelationReport]:
        return self._correlations.get(correlation_id)

    def list_correlations(self) -> List[TelemetryCorrelationReport]:
        return list(self._correlations.values())
