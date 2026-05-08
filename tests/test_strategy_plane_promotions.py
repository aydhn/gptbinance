import pytest
from app.strategy_plane.enums import LifecycleState
from app.strategy_plane.promotions import StrategyPromotionGovernance
from app.strategy_plane.exceptions import PromotionError


def test_promotion_governance():
    gov = StrategyPromotionGovernance()

    # Missing evidence for paper
    with pytest.raises(PromotionError):
        gov.evaluate_promotion(
            LifecycleState.REPLAY_QUALIFIED,
            LifecycleState.PAPER_CANDIDATE,
            evidence_bundle={},
        )

    # Valid evidence for paper
    assert (
        gov.evaluate_promotion(
            LifecycleState.REPLAY_QUALIFIED,
            LifecycleState.PAPER_CANDIDATE,
            evidence_bundle={"replay_performance_report": "some_ref"},
        )
        is True
    )
