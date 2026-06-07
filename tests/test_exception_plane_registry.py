import pytest
from app.exception_plane.registry import CanonicalExceptionRegistry
from app.exception_plane.models import ExceptionObject, ExceptionClass

def test_registry():
    registry = CanonicalExceptionRegistry()
    obj = ExceptionObject(
        exception_id="EX-100",
        exception_class=ExceptionClass.POLICY_WAIVER,
        owner="system",
        scope="global",
        deviation_posture="bounded",
        expiry_posture="enforced"
    )
    registry.register(obj)

    fetched = registry.get("EX-100")
    assert fetched.exception_id == "EX-100"
    assert fetched.exception_class == ExceptionClass.POLICY_WAIVER
