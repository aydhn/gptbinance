import pytest
from app.continuity_plane.forecasting import ContinuityForecaster
from app.continuity_plane.models import ContinuityForecastReport

def test_forecaster():
    forecaster = ContinuityForecaster()
    record = ContinuityForecastReport(
        service_id="srv_1",
        forecast_type="rto_miss",
        uncertainty_class="medium",
        description="Risk of RTO miss"
    )
    forecaster.record_forecast(record)

    retrieved = forecaster.get_forecast("srv_1")
    assert retrieved is not None
    assert retrieved.service_id == "srv_1"
