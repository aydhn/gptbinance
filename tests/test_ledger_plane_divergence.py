import pytest
from app.ledger_plane.divergence import DivergenceDetector
from app.ledger_plane.enums import DivergenceSeverity


def test_divergence_report_creation():
    report = DivergenceDetector.report(
        severity=DivergenceSeverity.HIGH,
        description="Runtime balance does not match venue balance",
    )
    assert report.severity == DivergenceSeverity.HIGH
    assert "Runtime balance" in report.description
