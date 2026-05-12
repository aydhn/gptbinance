import pytest
from app.observability_plane.quality import QualityAnalyzer

def test_quality_reporting():
    analyzer = QualityAnalyzer()
    analyzer.report_finding("t1", "missing_tag")
    assert analyzer.get_findings("t1") == ["missing_tag"]
