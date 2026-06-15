import pytest
from app.reliance_plane.repository import process_repository

def test_process_repository():
    result = process_repository({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "repository"
