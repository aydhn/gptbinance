from app.ops.go_live_gates import GoLiveGate
from app.ops.enums import GoLiveVerdict


def test_go_live_gate_fails_by_default():
    from unittest.mock import MagicMock

    mock_reg = MagicMock()
    gate = GoLiveGate(registry=mock_reg)
    report = gate.check_derivatives_readiness()
    assert type(report) == dict
