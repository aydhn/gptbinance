from datetime import datetime, timezone
from typing import List
from app.capacity_plane.models import CapacityEquivalenceReport
from app.capacity_plane.enums import WorkloadClass, EquivalenceVerdict

_equivalence_reports: List[CapacityEquivalenceReport] = []


def record_equivalence_report(
    report_id: str,
    workload_class: WorkloadClass,
    environments_compared: List[str],
    verdict: EquivalenceVerdict,
    divergence_sources: List[str],
    proof_notes: str,
) -> CapacityEquivalenceReport:
    rep = CapacityEquivalenceReport(
        report_id=report_id,
        workload_class=workload_class,
        environments_compared=environments_compared,
        verdict=verdict,
        divergence_sources=divergence_sources,
        proof_notes=proof_notes,
        timestamp=datetime.now(timezone.utc),
    )
    _equivalence_reports.append(rep)
    return rep


def list_equivalence_reports() -> List[CapacityEquivalenceReport]:
    return _equivalence_reports
