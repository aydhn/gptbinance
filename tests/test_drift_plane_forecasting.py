import pytest
from app.drift_plane.forecasting import ForecastingManager

def test_forecast_creation():
    manager = ForecastingManager()
    forecast = manager.create_forecast("recurrence_likelihood", "high", "High probability of recurrence.")

    assert forecast.forecast_type == "recurrence_likelihood"
    assert forecast.uncertainty_class == "high"
    assert forecast.details == "High probability of recurrence."
