from typing import Dict, List, Optional

from .models import ReliabilityEquivalenceReport


class EquivalenceManager:
    def __init__(self):
        self._reports: Dict[str, List[ReliabilityEquivalenceReport]] = {}

    def record_report(self, report: ReliabilityEquivalenceReport) -> None:
        if report.service_id not in self._reports:
            self._reports[report.service_id] = []
        self._reports[report.service_id].append(report)

    def get_latest_report(
        self, service_id: str
    ) -> Optional[ReliabilityEquivalenceReport]:
        reports = self._reports.get(service_id, [])
        if not reports:
            return None
        return reports[-1]
