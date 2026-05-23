from app.rights_plane.models import WaiverRecord, RightRecord
from app.rights_plane.enums import RightClass
from app.rights_plane.exceptions import InvalidWaiverError, InalienableRightOverrideError

def apply_waiver(waiver: WaiverRecord, right: RightRecord):
    if right.is_inalienable:
        raise InalienableRightOverrideError(f"Right {right.right_id} is inalienable and cannot be waived.")
    if waiver.representative_id and waiver.representative_id != right.holder_id:
        raise InvalidWaiverError("Waiver laundering detected: Signee does not have authority to waive.")
    return True
