from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityEquivalenceReport

class ContinuityEquivalenceAnalyzer:
    def __init__(self):
        self._reports: Dict[str, ContinuityEquivalenceReport] = {}

    def record_report(self, report: ContinuityEquivalenceReport) -> None:
        self._reports[report.service_id] = report

    def get_report(self, service_id: str) -> Optional[ContinuityEquivalenceReport]:
        return self._reports.get(service_id)
