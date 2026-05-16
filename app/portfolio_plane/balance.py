from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioBalanceReport
from app.portfolio_plane.exceptions import PortfolioStorageError

class BalanceManager:
    def __init__(self):
        self._reports: Dict[str, PortfolioBalanceReport] = {}

    def register(self, report: PortfolioBalanceReport):
        if report.report_id in self._reports:
            raise PortfolioStorageError(f"Balance Report {report.report_id} already exists")
        self._reports[report.report_id] = report

    def get(self, report_id: str) -> Optional[PortfolioBalanceReport]:
        return self._reports.get(report_id)

    def get_all(self) -> Dict[str, PortfolioBalanceReport]:
        return self._reports.copy()
