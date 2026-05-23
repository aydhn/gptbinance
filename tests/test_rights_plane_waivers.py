
import pytest
from app.rights_plane.waivers import apply_waiver
from app.rights_plane.models import WaiverRecord, RightRecord
from app.rights_plane.enums import RightClass, WaiverClass
from app.rights_plane.exceptions import InalienableRightOverrideError, InvalidWaiverError

def test_inalienable_right_cannot_be_waived():
    right = RightRecord(right_id="R-001", right_class=RightClass.ACCESS, holder_id="H1", is_inalienable=True)
    waiver = WaiverRecord(waiver_id="W-001", waiver_class=WaiverClass.SCOPED, right_ref="R-001", representative_id="H1")
    with pytest.raises(InalienableRightOverrideError):
        apply_waiver(waiver, right)

def test_invalid_representative_waiver():
    right = RightRecord(right_id="R-002", right_class=RightClass.ACCESS, holder_id="H1", is_inalienable=False)
    waiver = WaiverRecord(waiver_id="W-002", waiver_class=WaiverClass.SCOPED, right_ref="R-002", representative_id="H2")
    with pytest.raises(InvalidWaiverError):
        apply_waiver(waiver, right)
