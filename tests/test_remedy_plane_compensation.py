from app.remedy_plane.models import CompensationRecord
from app.remedy_plane.enums import CompensationClass

def test_compensation():
    c = CompensationRecord(compensation_id="c-1", compensation_class=CompensationClass.SERVICE_CREDIT, amount_or_value="$100", beneficiary="user1", target_harm_id="h-1", proof_notes="")
    assert c.amount_or_value == "$100"
