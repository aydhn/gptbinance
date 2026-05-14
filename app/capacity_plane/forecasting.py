from datetime import datetime, timezone
from typing import Dict, List, Optional
from app.capacity_plane.models import CapacityForecastReport

_forecasts: Dict[str, CapacityForecastReport] = {}


def record_forecast(
    target_id: str,
    forecast_type: str,
    exhaustion_eta_seconds: Optional[float],
    uncertainty_class: str,
) -> CapacityForecastReport:
    rec = CapacityForecastReport(
        target_id=target_id,
        forecast_type=forecast_type,
        exhaustion_eta_seconds=exhaustion_eta_seconds,
        uncertainty_class=uncertainty_class,
        timestamp=datetime.now(timezone.utc),
    )
    _forecasts[f"{target_id}_{forecast_type}"] = rec
    return rec


def list_forecasts() -> List[CapacityForecastReport]:
    return list(_forecasts.values())
