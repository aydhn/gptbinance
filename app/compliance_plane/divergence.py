from app.compliance_plane.models import ComplianceDivergenceReport
from typing import Dict, List


class DivergenceManager:
    def __init__(self):
        self._reports: Dict[str, ComplianceDivergenceReport] = {}

    def register_report(self, report: ComplianceDivergenceReport) -> None:
        self._reports[report.report_id] = report

    def list_reports(self) -> List[ComplianceDivergenceReport]:
        return list(self._reports.values())
