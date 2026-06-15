import pytest
from app.reliance_plane.dependency_use import process_dependency_use

def test_process_dependency_use():
    result = process_dependency_use({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "dependency_use"
