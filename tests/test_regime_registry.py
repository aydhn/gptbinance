import pytest
from app.research.regime.registry import RegimeRegistry
from app.research.regime.trend_regime import TrendPersistenceEvaluator
from app.research.regime.enums import RegimeFamily
from app.research.regime.exceptions import InvalidRegimeSpecError


def test_registry_registration():
    registry = RegimeRegistry()
    evaluator = TrendPersistenceEvaluator()

    registry.register("test_trend", evaluator)
    assert "test_trend" in registry.list_all_evaluators()

    with pytest.raises(InvalidRegimeSpecError):
        registry.register("test_trend", evaluator)


def test_registry_retrieval():
    registry = RegimeRegistry()
    evaluator = TrendPersistenceEvaluator()
    registry.register("test_trend", evaluator)

    retrieved = registry.get_evaluator("test_trend")
    assert retrieved.family == RegimeFamily.TREND

    family_evaluators = registry.get_evaluators_by_family(RegimeFamily.TREND)
    assert len(family_evaluators) == 1

    with pytest.raises(InvalidRegimeSpecError):
        registry.get_evaluator("non_existent")
