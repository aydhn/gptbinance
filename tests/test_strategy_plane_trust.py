import pytest
from app.strategy_plane.trust import StrategyTrustEvaluator
from app.strategy_plane.models import (
    StrategyDefinition,
    SignalContract,
    DependencyContract,
    StrategyEquivalenceReport,
    StrategyDecayReport,
    StrategyOverlapReport,
)
from app.strategy_plane.enums import (
    StrategyClass,
    StrategyFamily,
    LifecycleState,
    TrustVerdict,
    EquivalenceVerdict,
    DecaySeverity,
)


def test_trust_evaluation():
    evaluator = StrategyTrustEvaluator()

    sig = SignalContract(
        signal_id="sig",
        description="desc",
        expected_inputs=[],
        expected_semantics="sem",
        directionality="dir",
    )
    dep = DependencyContract(
        data_manifests=[], feature_manifests=[], model_manis=[], config_manifests=[]
    )
    strat = StrategyDefinition(
        strategy_id="strat-trust",
        strategy_class=StrategyClass.HEDGE,
        family=StrategyFamily.TREND_FOLLOWING,
        hypothesis_ref="hyp",
        thesis_ref="th-1",
        signal_contracts=[sig],
        dependencies=dep,
    )

    # Base trusted
    verdict = evaluator.evaluate(strat, LifecycleState.ACTIVE_FULL)
    assert verdict.verdict == TrustVerdict.TRUSTED

    # Frozen state
    verdict = evaluator.evaluate(strat, LifecycleState.FROZEN)
    assert verdict.verdict == TrustVerdict.BLOCKED

    # Critical decay
    decay = StrategyDecayReport(
        strategy_id="s",
        severity=DecaySeverity.CRITICAL,
        performance_decay="",
        capture_decay="",
        execution_drag_increase="",
        notes="",
    )
    verdict = evaluator.evaluate(strat, LifecycleState.ACTIVE_FULL, decay_report=decay)
    assert verdict.verdict == TrustVerdict.DEGRADED

    # Divergent equivalence
    eq = StrategyEquivalenceReport(
        strategy_id="s",
        verdict=EquivalenceVerdict.DIVERGENT,
        divergence_sources=[],
        notes="",
    )
    verdict = evaluator.evaluate(
        strat, LifecycleState.ACTIVE_FULL, equivalence_report=eq
    )
    assert verdict.verdict == TrustVerdict.BLOCKED
