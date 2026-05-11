from app.compliance_plane.models import ComplianceEquivalenceReport
from app.compliance_plane.enums import EquivalenceVerdict
from typing import Dict, List


class EquivalenceManager:
    def __init__(self):
        self._reports: Dict[str, ComplianceEquivalenceReport] = {}

    def register_report(self, report: ComplianceEquivalenceReport) -> None:
        self._reports[report.report_id] = report

    def list_reports(self) -> List[ComplianceEquivalenceReport]:
        return list(self._reports.values())
