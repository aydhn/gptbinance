import pytest
from app.exception_plane.trust import TrustedExceptionVerdictEngine
from app.exception_plane.models import ExceptionObject, ExceptionClass, TrustVerdictEnum

def test_trust_manager():
    engine = TrustedExceptionVerdictEngine()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = engine.evaluate_trust(obj)
    assert res.verdict == TrustVerdictEnum.TRUSTED
    assert "trigger clarity" in res.factors
