import pytest
from app.exception_plane.reporting import ReportingManager
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_reporting_manager():
    manager = ReportingManager()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = manager.evaluate(obj)
    assert res["exception_id"] == "EX-100"
    assert "proof_notes" in res
