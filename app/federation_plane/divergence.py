from typing import Dict, List, Optional
from app.federation_plane.models import FederationDivergenceReport
from app.federation_plane.exceptions import FederationPlaneError


class DivergenceManager:
    def __init__(self):
        self._reports: Dict[str, FederationDivergenceReport] = {}

    def register(self, report: FederationDivergenceReport):
        if not report.report_id:
            raise FederationPlaneError("Report ID required.")
        self._reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[FederationDivergenceReport]:
        return self._reports.get(report_id)

    def list_reports(self) -> List[FederationDivergenceReport]:
        return list(self._reports.values())
