from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioEquivalenceReport
from app.portfolio_plane.exceptions import PortfolioStorageError

class EquivalenceManager:
    def __init__(self):
        self._reports: Dict[str, PortfolioEquivalenceReport] = {}

    def register(self, report: PortfolioEquivalenceReport):
        if report.report_id in self._reports:
            raise PortfolioStorageError(f"Equivalence Report {report.report_id} already exists")
        self._reports[report.report_id] = report

    def get(self, report_id: str) -> Optional[PortfolioEquivalenceReport]:
        return self._reports.get(report_id)

    def get_all(self) -> Dict[str, PortfolioEquivalenceReport]:
        return self._reports.copy()
