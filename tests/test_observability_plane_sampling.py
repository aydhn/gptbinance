import pytest
from app.observability_plane.sampling import SamplingRegistry
from app.observability_plane.models import SamplingRecord
from app.observability_plane.enums import SamplingClass
from app.observability_plane.exceptions import InvalidSamplingDefinitionError

def test_sampling_rate_enforcement():
    reg = SamplingRegistry()
    with pytest.raises(InvalidSamplingDefinitionError):
        reg.register_sampling(SamplingRecord(telemetry_id="t1", sampling_class=SamplingClass.RATE, sampling_rate=0.0))

    reg.register_sampling(SamplingRecord(telemetry_id="t1", sampling_class=SamplingClass.RATE, sampling_rate=0.5))
    assert reg.get_sampling("t1").sampling_rate == 0.5
