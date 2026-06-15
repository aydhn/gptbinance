import pytest
from app.reliance_plane.policy import process_policy

def test_process_policy():
    result = process_policy({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "policy"
