import pytest
from app.strategy_plane.models import (
    StrategyDefinition,
    SignalContract,
    DependencyContract,
)
from app.strategy_plane.enums import StrategyClass, StrategyFamily
from app.strategy_plane.exceptions import InvalidStrategyDefinition
from app.strategy_plane.registry import CanonicalStrategyRegistry


def test_registry_registration():
    registry = CanonicalStrategyRegistry()
    sig = SignalContract(
        signal_id="test-sig",
        description="Test",
        expected_inputs=["in1"],
        expected_semantics="binary",
        directionality="long",
    )
    dep = DependencyContract(
        data_manifests=[], feature_manifests=[], model_manis=[], config_manifests=[]
    )

    definition = StrategyDefinition(
        strategy_id="strat-1",
        strategy_class=StrategyClass.HEDGE,
        family=StrategyFamily.TREND_FOLLOWING,
        hypothesis_ref="hyp-1",
        thesis_ref="th-1",
        signal_contracts=[sig],
        dependencies=dep,
    )

    registry.register(definition)
    assert registry.get("strat-1") is not None
    assert registry.get("strat-1").strategy_id == "strat-1"

    with pytest.raises(InvalidStrategyDefinition):
        registry.register(definition)  # Duplicate


def test_registry_validation():
    registry = CanonicalStrategyRegistry()
    dep = DependencyContract(
        data_manifests=[], feature_manifests=[], model_manis=[], config_manifests=[]
    )

    # Missing hypothesis
    with pytest.raises(InvalidStrategyDefinition):
        registry.register(
            StrategyDefinition(
                strategy_id="strat-2",
                strategy_class=StrategyClass.HEDGE,
                family=StrategyFamily.TREND_FOLLOWING,
                hypothesis_ref="",
                thesis_ref="th-1",
                signal_contracts=[
                    SignalContract(
                        signal_id="sig",
                        description="desc",
                        expected_inputs=[],
                        expected_semantics="sem",
                        directionality="dir",
                    )
                ],
                dependencies=dep,
            )
        )

    # Missing signal contract
    with pytest.raises(InvalidStrategyDefinition):
        registry.register(
            StrategyDefinition(
                strategy_id="strat-3",
                strategy_class=StrategyClass.HEDGE,
                family=StrategyFamily.TREND_FOLLOWING,
                hypothesis_ref="hyp",
                thesis_ref="th-1",
                signal_contracts=[],
                dependencies=dep,
            )
        )
