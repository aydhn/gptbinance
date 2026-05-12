import pytest
from app.observability_plane.normalization import NormalizationRegistry
from app.observability_plane.models import TelemetryNormalizationRecord
from app.observability_plane.exceptions import ObservabilityPlaneError

def test_normalization_rewrite_enforcement():
    reg = NormalizationRegistry()
    with pytest.raises(ObservabilityPlaneError):
        reg.register_normalization(TelemetryNormalizationRecord(normalization_id="n1", telemetry_id="t1", semantic_rewrite=True))

    reg.register_normalization(TelemetryNormalizationRecord(normalization_id="n1", telemetry_id="t1", semantic_rewrite=False))
    assert reg.get_normalization("n1").semantic_rewrite is False
