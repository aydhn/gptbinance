from app.remedy_plane.models import BreachHarmRecord

def test_breach_harm():
    b = BreachHarmRecord(breach_harm_id="b-1", original_harm_id="h-1", breach_type="sla_breach", commitment_ref="c-1", description="delayed", proof_notes="")
    assert b.breach_type == "sla_breach"
