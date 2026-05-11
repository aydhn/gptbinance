import pytest
from app.policy_plane.divergence import report_divergence


def test_report_divergence():
    report = report_divergence("paper", "live", "Different policy version", "high")
    assert report is not None
    assert report.source_environment == "paper"
    assert report.target_environment == "live"
    assert report.severity == "high"
