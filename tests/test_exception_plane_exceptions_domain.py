import pytest
from app.exception_plane.exceptions_domain import ExceptionsDomainManager
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_exceptions_domain_manager():
    manager = ExceptionsDomainManager()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = manager.evaluate(obj)
    assert res["exception_id"] == "EX-100"
    assert "proof_notes" in res
