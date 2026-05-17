import pytest
from app.environment_plane.equivalence import evaluate_equivalence
from app.environment_plane.enums import EquivalenceVerdict

def test_evaluate_equivalence():
    equiv = evaluate_equivalence(EquivalenceVerdict.EQUIVALENT, "Matches 1:1")
    assert equiv.verdict == EquivalenceVerdict.EQUIVALENT
    assert equiv.proof_notes == "Matches 1:1"
