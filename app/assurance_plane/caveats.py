from app.assurance_plane.models import CaveatRecord
from app.assurance_plane.enums import CaveatClass

def create_caveat(caveat_id: str, assurance_id: str, caveat_class: CaveatClass, description: str) -> CaveatRecord:
    return CaveatRecord(
        caveat_id=caveat_id,
        assurance_id=assurance_id,
        caveat_class=caveat_class,
        description=description
    )
