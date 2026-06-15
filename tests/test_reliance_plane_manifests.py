import pytest
from app.reliance_plane.manifests import process_manifests

def test_process_manifests():
    result = process_manifests({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "manifests"
