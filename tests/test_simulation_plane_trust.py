from app.simulation_plane.trust import TrustedVerdictEngine
from app.simulation_plane.enums import TrustVerdict


def test_trust():
    evaluator = TrustedVerdictEngine()
    report = evaluator.evaluate("run1", {"issue": "hidden_assumption"})
    assert report.verdict == TrustVerdict.CAUTION
