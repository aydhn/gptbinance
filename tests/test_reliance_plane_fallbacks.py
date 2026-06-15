import pytest
from app.reliance_plane.fallbacks import process_fallbacks

def test_process_fallbacks():
    result = process_fallbacks({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "fallbacks"
