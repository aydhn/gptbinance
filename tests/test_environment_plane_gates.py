import pytest
from app.environment_plane.gates import evaluate_gate

def test_evaluate_gate():
    gate = evaluate_gate("ParityCheck", True, "ref123")
    assert gate.gate_name == "ParityCheck"
    assert gate.passed is True
    assert gate.lineage_refs == "ref123"
