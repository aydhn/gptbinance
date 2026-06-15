import pytest
from app.reliance_plane.compensating_review import process_compensating_review

def test_process_compensating_review():
    result = process_compensating_review({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "compensating_review"
