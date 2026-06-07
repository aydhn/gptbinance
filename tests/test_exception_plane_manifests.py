import pytest
from app.exception_plane.manifests import ManifestsManager
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_manifests_manager():
    manager = ManifestsManager()
    obj = ExceptionObject(exception_id="EX-100", exception_class=ExceptionClass.POLICY_WAIVER, owner="system", scope="global", deviation_posture="bounded", expiry_posture="enforced")
    res = manager.evaluate(obj)
    assert res["exception_id"] == "EX-100"
    assert "proof_notes" in res
