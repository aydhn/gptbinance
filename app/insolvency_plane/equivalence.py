# equivalence.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import InsolvencyEquivalenceReport

class InsolvencyEquivalenceManager:
    def __init__(self):
        self.reports: Dict[str, InsolvencyEquivalenceReport] = {}

    def register_report(self, report: InsolvencyEquivalenceReport):
        self.reports[report.report_id] = report

    def get_report(self, report_id: str) -> Optional[InsolvencyEquivalenceReport]:
        return self.reports.get(report_id)

    def list_reports(self) -> List[InsolvencyEquivalenceReport]:
        return list(self.reports.values())
