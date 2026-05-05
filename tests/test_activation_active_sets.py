import pytest
from app.activation.active_sets import ActiveSetRegistry
from app.activation.models import ActivationScope
from app.activation.enums import ActivationStage, ActiveSetStatus
from app.activation.exceptions import ActiveSetConflictError


def test_activate_supersedes_correctly():
    registry = ActiveSetRegistry()
    scope = ActivationScope(allowed_profiles=["test_profile"])

    record1 = registry.activate(
        "intent-1", "cand-1", scope, ActivationStage.STAGE_0_OBSERVE
    )
    assert record1.status == ActiveSetStatus.ACTIVE

    # Activate same profile with new intent
    record2 = registry.activate(
        "intent-2", "cand-2", scope, ActivationStage.STAGE_0_OBSERVE
    )

    # Check current snapshot
    active_records = registry.current_snapshot.active_records

    assert len(active_records) == 2
    rec1_updated = next(r for r in active_records if r.intent_id == "intent-1")
    assert rec1_updated.status == ActiveSetStatus.SUPERSEDED
    assert record2.status == ActiveSetStatus.ACTIVE
