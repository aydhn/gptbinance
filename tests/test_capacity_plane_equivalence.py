from app.capacity_plane.equivalence import (
    record_equivalence_report,
    list_equivalence_reports,
)
from app.capacity_plane.enums import WorkloadClass, EquivalenceVerdict


def test_equivalence_report():
    record_equivalence_report(
        "eq_rep_1",
        WorkloadClass.LIVE_TRADING,
        ["live", "replay"],
        EquivalenceVerdict.PARTIAL,
        ["quota limit differences"],
        "Tested partial equivalence",
    )
    reps = list_equivalence_reports()
    assert len(reps) > 0
    assert reps[-1].verdict == EquivalenceVerdict.PARTIAL
