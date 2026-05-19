from typing import Dict, List, Optional
from app.federation_plane.models import FederationEquivalenceReport
from app.federation_plane.exceptions import FederationPlaneError


class EquivalenceManager:
    def __init__(self):
        self._reports: Dict[str, FederationEquivalenceReport] = {}

    def register(self, report: FederationEquivalenceReport):
        if not report.report_id:
            raise FederationPlaneError("Report ID required.")
        self._reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[FederationEquivalenceReport]:
        return self._reports.get(report_id)

    def list_reports(self) -> List[FederationEquivalenceReport]:
        return list(self._reports.values())
