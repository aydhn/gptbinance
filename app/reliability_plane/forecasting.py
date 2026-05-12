from datetime import datetime
from typing import Dict, List, Optional

from .models import ReliabilityForecastReport


class ForecastManager:
    def __init__(self):
        self._reports: Dict[str, List[ReliabilityForecastReport]] = {}

    def record_forecast(self, report: ReliabilityForecastReport) -> None:
        if report.service_id not in self._reports:
            self._reports[report.service_id] = []
        self._reports[report.service_id].append(report)

    def get_latest_forecast(
        self, service_id: str
    ) -> Optional[ReliabilityForecastReport]:
        reports = self._reports.get(service_id, [])
        if not reports:
            return None
        return sorted(reports, key=lambda r: r.timestamp)[-1]
