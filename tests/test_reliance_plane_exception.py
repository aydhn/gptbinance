import pytest
from app.reliance_plane.exception import process_exception

def test_process_exception():
    result = process_exception({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "exception"
