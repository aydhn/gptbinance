import pytest
from app.environment_plane.capabilities import define_capabilities

def test_define_capabilities():
    caps = define_capabilities(["read", "write"], "No destructive tests")
    assert "read" in caps.capabilities
    assert caps.caveats == "No destructive tests"
