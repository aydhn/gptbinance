import pytest
from app.value_plane.models import RoiRecord
from app.value_plane.roi import roi_registry
from app.value_plane.enums import RoiClass
from app.value_plane.exceptions import InvalidRoiRecord

def test_roi_record():
    record = RoiRecord(
        roi_id="roi_1",
        roi_class=RoiClass.NET_ROI,
        gross_roi=1.5,
        net_roi=1.2,
        payback_horizon="12m",
        denominator_quality="high",
        cost_linkage="cost_1",
        roi_proof_notes="Tested"
    )
    roi_registry.register(record)
    assert roi_registry.get("roi_1") is not None

def test_invalid_roi_record():
    with pytest.raises(InvalidRoiRecord):
        record = RoiRecord(
            roi_id="roi_2",
            roi_class=RoiClass.NET_ROI,
            payback_horizon="12m",
            denominator_quality="high",
            cost_linkage="",
            roi_proof_notes="Tested"
        )
        roi_registry.register(record)
