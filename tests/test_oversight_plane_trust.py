from app.oversight_plane.trust import evaluate_oversight_trust
from app.oversight_plane.models import OversightRecord
from app.oversight_plane.enums import TrustVerdictEnum

def test_trust_evaluation():
    rec = OversightRecord(
        oversight_id="OV-002",
        class_type="authoritative",
        owner="admin",
        scope_ref="full",
        scrutiny_posture="light",
        intervention_posture="advisory"
    )
    trust = evaluate_oversight_trust(rec)
    assert trust.verdict == TrustVerdictEnum.TRUSTED
