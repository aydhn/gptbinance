import pytest
from app.strategy_plane.storage import StrategyPlaneStorage
from app.strategy_plane.models import StrategyHypothesis


def test_storage():
    storage = StrategyPlaneStorage()
    hyp = StrategyHypothesis(
        hypothesis_id="hyp-test",
        behavioral_claim="claim",
        expected_edge_reason="reason",
        expected_regimes=[],
        invalidation_conditions=[],
        lineage_refs=[],
    )
    storage.save_hypothesis(hyp)
    assert storage.hypotheses["hyp-test"].behavioral_claim == "claim"
