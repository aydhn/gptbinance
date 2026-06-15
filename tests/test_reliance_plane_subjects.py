import pytest
from app.reliance_plane.subjects import process_subjects

def test_process_subjects():
    result = process_subjects({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "subjects"
