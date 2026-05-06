from uuid import uuid4
from app.identity.enums import BreakglassClass
from app.identity.breakglass import breakglass_manager


def test_breakglass_activation_and_review():
    principal_id = uuid4()
    record = breakglass_manager.activate(
        principal_id, "System down", BreakglassClass.EMERGENCY_HALT
    )

    assert record.reviewed_at is None

    reviewer_id = uuid4()
    success = breakglass_manager.review(record.record_id, reviewer_id)

    assert success == True
    assert record.reviewed_at is not None
