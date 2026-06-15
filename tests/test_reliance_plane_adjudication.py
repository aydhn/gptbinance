import pytest
from app.reliance_plane.adjudication import process_adjudication

def test_process_adjudication():
    result = process_adjudication({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "adjudication"
