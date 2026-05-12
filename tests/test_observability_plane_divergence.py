import pytest
from app.observability_plane.divergence import DivergenceAnalyzer
from app.observability_plane.models import ObservabilityDivergenceReport

def test_divergence_reporting():
    analyzer = DivergenceAnalyzer()
    analyzer.report_divergence(ObservabilityDivergenceReport(report_id="r1", divergence_sources=["s1"]))
    assert analyzer.get_report("r1").divergence_sources == ["s1"]
