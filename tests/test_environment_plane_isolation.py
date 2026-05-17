import pytest
from app.environment_plane.isolation import define_isolation
from app.environment_plane.enums import IsolationClass

def test_define_isolation():
    iso = define_isolation(IsolationClass.COMPUTE, "Verified compute isolation")
    assert iso.isolation_class == IsolationClass.COMPUTE
    assert iso.proof_notes == "Verified compute isolation"
