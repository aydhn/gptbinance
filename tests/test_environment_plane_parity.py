import pytest
from app.environment_plane.parity import evaluate_parity
from app.environment_plane.enums import ParityClass

def test_evaluate_parity():
    parity = evaluate_parity(ParityClass.HIGH_PARITY, "Sufficient for testing")
    assert parity.parity_class == ParityClass.HIGH_PARITY
    assert parity.sufficiency_notes == "Sufficient for testing"
