from app.rights_plane.models import RightRecord
from app.rights_plane.enums import RightClass

def process_remedy(right: RightRecord, remedy_applied: bool):
    if right.right_class == RightClass.CHALLENGE:
        right.is_exhausted = False
        return "survival: challenge right remains open"
    right.is_exhausted = remedy_applied
    return "exhausted"
