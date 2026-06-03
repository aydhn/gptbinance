from app.remedy_plane.models import ContainmentRecord
from app.remedy_plane.enums import ContainmentClass

def test_containment():
    c = ContainmentRecord(containment_id="c-1", containment_class=ContainmentClass.BLAST_RADIUS_CONTAINMENT, description="desc", target_harm_id="h-1", is_rollback=True, caveats="")
    assert c.is_rollback
