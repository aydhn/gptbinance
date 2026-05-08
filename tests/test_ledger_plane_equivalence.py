import pytest
from app.ledger_plane.equivalence import EquivalenceEvaluator
from app.ledger_plane.enums import EquivalenceVerdict

def test_equivalence_report_creation():
    report = EquivalenceEvaluator.evaluate(
        verdict=EquivalenceVerdict.PARTIAL,
        description="Shadow ledger matches partial paper trade history"
    )
    assert report.verdict == EquivalenceVerdict.PARTIAL
    assert "Shadow ledger" in report.description
