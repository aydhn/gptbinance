import pytest
from app.strategy_plane.enums import LifecycleState
from app.strategy_plane.lifecycle import StrategyLifecycleEvaluator
from app.strategy_plane.exceptions import InvalidLifecycleTransition


def test_lifecycle_transitions():
    evaluator = StrategyLifecycleEvaluator()

    # Initial state should be HYPOTHESIS_ONLY implicitly
    assert evaluator.get_current_state("strat-test") == LifecycleState.HYPOTHESIS_ONLY

    # Valid transition
    evaluator.transition(
        "strat-test", LifecycleState.RESEARCH_CANDIDATE, "ready for research"
    )
    assert (
        evaluator.get_current_state("strat-test") == LifecycleState.RESEARCH_CANDIDATE
    )

    # Invalid jump
    with pytest.raises(InvalidLifecycleTransition):
        evaluator.transition("strat-test", LifecycleState.ACTIVE_FULL, "skipped steps")

    evaluator.transition("strat-test", LifecycleState.REPLAY_QUALIFIED, "replay passed")
    evaluator.transition(
        "strat-test", LifecycleState.PAPER_CANDIDATE, "ready for paper"
    )
    assert evaluator.get_current_state("strat-test") == LifecycleState.PAPER_CANDIDATE
