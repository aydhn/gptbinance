from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioDivergenceReport
from app.portfolio_plane.exceptions import PortfolioStorageError

class DivergenceManager:
    def __init__(self):
        self._reports: Dict[str, PortfolioDivergenceReport] = {}

    def register(self, report: PortfolioDivergenceReport):
        if report.report_id in self._reports:
            raise PortfolioStorageError(f"Divergence Report {report.report_id} already exists")
        self._reports[report.report_id] = report

    def get(self, report_id: str) -> Optional[PortfolioDivergenceReport]:
        return self._reports.get(report_id)

    def get_all(self) -> Dict[str, PortfolioDivergenceReport]:
        return self._reports.copy()
