from typing import Dict, List, Optional
from .models import ObservabilityDivergenceReport

class DivergenceAnalyzer:
    def __init__(self):
        self._reports: Dict[str, ObservabilityDivergenceReport] = {}

    def report_divergence(self, report: ObservabilityDivergenceReport) -> None:
        self._reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[ObservabilityDivergenceReport]:
        return self._reports.get(report_id)

    def list_reports(self) -> List[ObservabilityDivergenceReport]:
        return list(self._reports.values())
