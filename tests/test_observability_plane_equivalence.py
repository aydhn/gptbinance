import pytest
from app.observability_plane.equivalence import EquivalenceAnalyzer
from app.observability_plane.models import ObservabilityEquivalenceReport
from app.observability_plane.enums import EquivalenceVerdict

def test_equivalence_reporting():
    analyzer = EquivalenceAnalyzer()
    analyzer.report_equivalence(ObservabilityEquivalenceReport(report_id="r1", verdict=EquivalenceVerdict.EQUIVALENT))
    assert analyzer.get_report("r1").verdict == EquivalenceVerdict.EQUIVALENT
