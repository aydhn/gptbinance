import pytest
from app.activation.reverts import RevertPlanner
from app.activation.repository import ActivationRepository
from app.activation.models import ActiveSetRecord, ActiveSetSnapshot, ActivationScope
from app.activation.enums import ActivationStage, RevertClass, ActiveSetStatus


class MockRepo(ActivationRepository):
    def get_snapshot(self, snapshot_id: str):
        scope = ActivationScope(allowed_profiles=["prof1"])

        # Prior
        r1 = ActiveSetRecord(
            record_id="rec-1",
            intent_id="intent-prior",
            candidate_id="cand-1",
            scope=scope,
            stage=ActivationStage.STAGE_0_OBSERVE,
        )
        r1.status = ActiveSetStatus.SUPERSEDED

        # Current
        r2 = ActiveSetRecord(
            record_id="rec-2",
            intent_id="intent-fail",
            candidate_id="cand-2",
            scope=scope,
            stage=ActivationStage.STAGE_0_OBSERVE,
        )
        r2.status = ActiveSetStatus.ACTIVE

        return ActiveSetSnapshot(snapshot_id="snap-1", active_records=[r1, r2])


def test_revert_planner_full_revert():
    repo = MockRepo()
    planner = RevertPlanner(repo)
    plan = planner.plan_revert("intent-fail")

    assert plan.revert_class == RevertClass.FULL_REVERT
    assert plan.prior_active_set_ref == "rec-1"
