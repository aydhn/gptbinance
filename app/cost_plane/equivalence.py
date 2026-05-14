from app.cost_plane.models import CostEquivalenceReport
from app.cost_plane.enums import CostEquivalenceVerdict
import uuid

class EquivalenceManager:
    def __init__(self):
        self._reports: list[CostEquivalenceReport] = []

    def evaluate_equivalence(self, workload_ref: str, environments: list[str], verdict: CostEquivalenceVerdict, divergence_sources: list[str] = None) -> CostEquivalenceReport:
        report = CostEquivalenceReport(
            report_id=str(uuid.uuid4()),
            workload_ref=workload_ref,
            environments_compared=environments,
            verdict=verdict,
            divergence_sources=divergence_sources or []
        )
        self._reports.append(report)
        return report

    def list_reports(self) -> list[CostEquivalenceReport]:
        return self._reports
