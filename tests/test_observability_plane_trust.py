import pytest
from app.observability_plane.trust import TrustVerdictEngine
from app.observability_plane.models import ObservabilityTrustVerdict
from app.observability_plane.enums import TrustVerdict

def test_trust_reporting():
    engine = TrustVerdictEngine()
    engine.report_verdict("ctx1", ObservabilityTrustVerdict(verdict=TrustVerdict.TRUSTED, factors={"f1": "v1"}))
    assert engine.get_verdict("ctx1").verdict == TrustVerdict.TRUSTED
