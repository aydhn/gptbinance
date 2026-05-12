from datetime import datetime, timedelta
from typing import Dict, List, Optional

from .enums import BurnRateClass
from .models import BurnRateReport


class BurnRateManager:
    def __init__(self):
        self._reports: Dict[str, List[BurnRateReport]] = {}

    def record_report(self, report: BurnRateReport) -> None:
        if report.policy_id not in self._reports:
            self._reports[report.policy_id] = []
        self._reports[report.policy_id].append(report)

    def get_latest_report(self, policy_id: str) -> Optional[BurnRateReport]:
        reports = self._reports.get(policy_id, [])
        if not reports:
            return None
        return sorted(reports, key=lambda r: r.timestamp)[-1]

    def list_reports(self, policy_id: str) -> List[BurnRateReport]:
        return sorted(self._reports.get(policy_id, []), key=lambda r: r.timestamp)

    def calculate_burn_rate_class(
        self, current_burn: float, short_burn: float, long_burn: float
    ) -> BurnRateClass:
        # A very basic example logic to determine class
        if current_burn > 10.0 or short_burn > 10.0:
            return BurnRateClass.CRITICAL
        elif current_burn > 2.0 or long_burn > 2.0:
            return BurnRateClass.ELEVATED
        return BurnRateClass.NOMINAL
