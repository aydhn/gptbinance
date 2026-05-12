from typing import Dict, List, Optional

from .models import ReliabilityDivergenceReport


class DivergenceManager:
    def __init__(self):
        self._reports: Dict[str, List[ReliabilityDivergenceReport]] = {}

    def record_report(self, report: ReliabilityDivergenceReport) -> None:
        if report.service_id not in self._reports:
            self._reports[report.service_id] = []
        self._reports[report.service_id].append(report)

    def get_latest_report(
        self, service_id: str
    ) -> Optional[ReliabilityDivergenceReport]:
        reports = self._reports.get(service_id, [])
        if not reports:
            return None
        return reports[-1]
