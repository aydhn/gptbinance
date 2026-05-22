from typing import List, Dict, Any
from app.adversarial_plane.models import AdversarialDivergenceReport

class DivergenceManager:
    def __init__(self):
        self._reports = {}

    def add_report(self, report: AdversarialDivergenceReport):
        self._reports[report.report_id] = report

    def get_report(self, report_id: str) -> AdversarialDivergenceReport:
        return self._reports.get(report_id)

    def list_reports(self) -> List[AdversarialDivergenceReport]:
        return list(self._reports.values())
