import pytest
from datetime import datetime, timezone
from app.continuity_plane.equivalence import ContinuityEquivalenceAnalyzer
from app.continuity_plane.models import ContinuityEquivalenceReport
from app.continuity_plane.enums import ContinuityEquivalenceVerdict

def test_equivalence_analyzer():
    analyzer = ContinuityEquivalenceAnalyzer()
    report = ContinuityEquivalenceReport(
        service_id="srv_1",
        verdict=ContinuityEquivalenceVerdict.EQUIVALENT,
        timestamp=datetime.now(timezone.utc)
    )
    analyzer.record_report(report)

    retrieved = analyzer.get_report("srv_1")
    assert retrieved is not None
    assert retrieved.verdict == ContinuityEquivalenceVerdict.EQUIVALENT
