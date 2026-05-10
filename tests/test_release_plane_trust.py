import pytest
from app.release_plane.trust import ReleaseTrustEngine
from app.release_plane.enums import TrustVerdict

class MockQuality:
    def __init__(self, passed, issues):
        self.passed = passed
        self.issues = issues

class MockEquivalence:
    def __init__(self, verdict):
        self.verdict = verdict

def test_trust_verdict():
    engine = ReleaseTrustEngine()

    # Trusted
    v1 = engine.synthesize_verdict("c1", MockQuality(True, []), MockEquivalence("equivalent"))
    assert v1.verdict == TrustVerdict.TRUSTED

    # Caution
    v2 = engine.synthesize_verdict("c2", MockQuality(False, ["Stale candidate"]), MockEquivalence("equivalent"))
    assert v2.verdict == TrustVerdict.CAUTION

    # Degraded
    v3 = engine.synthesize_verdict("c3", MockQuality(True, []), MockEquivalence("divergent"))
    assert v3.verdict == TrustVerdict.DEGRADED

    # Blocked
    v4 = engine.synthesize_verdict("c4", MockQuality(False, ["Missing Pins"]), MockEquivalence("equivalent"))
    assert v4.verdict == TrustVerdict.BLOCKED
