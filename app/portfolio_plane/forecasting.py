from typing import Dict, Optional
from app.portfolio_plane.models import PortfolioForecastReport
from app.portfolio_plane.exceptions import PortfolioStorageError

class ForecastingManager:
    def __init__(self):
        self._reports: Dict[str, PortfolioForecastReport] = {}

    def register(self, report: PortfolioForecastReport):
        if report.forecast_id in self._reports:
            raise PortfolioStorageError(f"Forecast {report.forecast_id} already exists")
        self._reports[report.forecast_id] = report

    def get(self, report_id: str) -> Optional[PortfolioForecastReport]:
        return self._reports.get(report_id)

    def get_all(self) -> Dict[str, PortfolioForecastReport]:
        return self._reports.copy()
