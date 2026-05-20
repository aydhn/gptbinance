import pytest
from app.provenance_plane.forecasting import forecast_provenance_decay
from app.provenance_plane.registry import registry

def test_forecast_provenance_decay():
    registry.register("obj-1", {"provenance_id": "obj-1", "decay_forecast": "STABLE"})
    assert forecast_provenance_decay("obj-1") == "STABLE"
