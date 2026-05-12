from typing import Dict, List, Optional

from .models import DependencyGraphNode, DependencyImpactReport


class DependencyManager:
    def __init__(self, registry):
        self._registry = registry
        self._impact_reports: Dict[str, List[DependencyImpactReport]] = {}

    def get_dependencies(self, service_id: str) -> List[DependencyGraphNode]:
        service = self._registry.get_service(service_id)
        if service:
            return service.dependencies
        return []

    def record_impact_report(self, report: DependencyImpactReport) -> None:
        if report.service_id not in self._impact_reports:
            self._impact_reports[report.service_id] = []
        self._impact_reports[report.service_id].append(report)

    def get_latest_impact_report(
        self, service_id: str
    ) -> Optional[DependencyImpactReport]:
        reports = self._impact_reports.get(service_id, [])
        if not reports:
            return None
        return reports[-1]

    def list_impact_reports(self, service_id: str) -> List[DependencyImpactReport]:
        return self._impact_reports.get(service_id, [])
