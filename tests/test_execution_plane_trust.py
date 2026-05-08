from app.execution_plane.trust import TrustVerdictEngine
from app.execution_plane.enums import TrustedExecutionVerdictClass

def test_trust_engine():
    t1 = TrustVerdictEngine.evaluate("m1", [], "clean", 100)
    assert t1.verdict == TrustedExecutionVerdictClass.TRUSTED

    t2 = TrustVerdictEngine.evaluate("m2", ["policy_block"], "clean", 100)
    assert t2.verdict == TrustedExecutionVerdictClass.BLOCKED

    t3 = TrustVerdictEngine.evaluate("m3", [], "degraded", 40)
    assert t3.verdict == TrustedExecutionVerdictClass.DEGRADED
