from app.ops.go_live_gates import GoLiveGate
from app.ops.enums import GoLiveVerdict


def test_go_live_gate_fails_by_default():
    gate = GoLiveGate()
    report = gate.evaluate("run-xyz")
    assert report.verdict == GoLiveVerdict.FAIL
    assert len(report.blockers) > 0
