import pytest
from app.reliance_plane.forecasting import process_forecasting

def test_process_forecasting():
    result = process_forecasting({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "forecasting"
