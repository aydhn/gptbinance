from typing import Dict, List, Optional
from app.continuity_plane.models import ContinuityDivergenceReport

class ContinuityDivergenceAnalyzer:
    def __init__(self):
        self._reports: Dict[str, ContinuityDivergenceReport] = {}

    def record_report(self, report: ContinuityDivergenceReport) -> None:
        self._reports[f"{report.service_id}_{report.divergence_source}"] = report

    def list_reports_for_service(self, service_id: str) -> List[ContinuityDivergenceReport]:
        return [r for r in self._reports.values() if r.service_id == service_id]
