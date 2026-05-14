from app.capacity_plane.saturation import record_saturation, list_saturation_records
from app.capacity_plane.enums import SaturationSeverity


def test_saturation_record():
    record_saturation(
        "gpu_pool_1",
        SaturationSeverity.EXHAUSTED,
        300.0,
        ["model_inference", "research"],
    )
    records = list_saturation_records()
    assert len(records) > 0
    assert records[-1].severity == SaturationSeverity.EXHAUSTED
