from app.remedy_plane.models import CureRecord
from app.remedy_plane.enums import CureClass

def test_cure_record():
    c = CureRecord(cure_id="c-1", cure_class=CureClass.PARTIAL_CURE, description="partial", target_harm_id="h-1", proof_notes="")
    assert c.cure_class == CureClass.PARTIAL_CURE
