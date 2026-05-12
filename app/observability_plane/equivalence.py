from typing import Dict, List, Optional
from .models import ObservabilityEquivalenceReport

class EquivalenceAnalyzer:
    def __init__(self):
        self._reports: Dict[str, ObservabilityEquivalenceReport] = {}

    def report_equivalence(self, report: ObservabilityEquivalenceReport) -> None:
        self._reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[ObservabilityEquivalenceReport]:
        return self._reports.get(report_id)

    def list_reports(self) -> List[ObservabilityEquivalenceReport]:
        return list(self._reports.values())
