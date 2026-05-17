import pytest
from app.environment_plane.limitations import define_limitations

def test_define_limitations():
    limits = define_limitations(["missing_external_api"], "External API is mocked")
    assert "missing_external_api" in limits.limitations
    assert limits.burden_notes == "External API is mocked"
