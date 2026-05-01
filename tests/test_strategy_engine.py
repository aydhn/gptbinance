from datetime import datetime, timezone
from app.strategies.engine import StrategyEngine
from app.strategies.models import (
    StrategySpec,
    StrategyContext,
    StrategyEvaluationResult,
    EntryIntentCandidate,
)
from app.strategies.enums import StrategyType, SignalDirection
from app.strategies.base import BaseStrategy
from app.strategies.registry import StrategyRegistry


class MockStrat(BaseStrategy):
    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        res = StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )
        if context.features.get("trigger"):
            res.entry_intent = EntryIntentCandidate(
                strategy_name=self.name,
                symbol=context.symbol,
                timestamp=context.timestamp,
                direction=SignalDirection.LONG,
                score=90,
                confidence=1.0,
            )
        return res


def test_strategy_engine():
    StrategyRegistry.register("mock_strat", MockStrat)
    spec = StrategySpec(name="mock_strat", strategy_type=StrategyType.UNKNOWN)
    StrategyRegistry.register_spec(spec)

    engine = StrategyEngine()
    engine.initialize_strategies([spec])

    now = datetime.now(timezone.utc)

    # Test no trigger
    batch = engine.evaluate("BTC", "15m", now, {"trigger": False})
    assert len(batch.raw_entry_intents) == 0

    # Test trigger
    batch = engine.evaluate("BTC", "15m", now, {"trigger": True})
    assert len(batch.raw_entry_intents) == 1
    assert batch.resolved_entry_intent is not None

    # Test cooldown prevents immediate re-trigger
    batch = engine.evaluate("BTC", "15m", now, {"trigger": True})
    assert len(batch.raw_entry_intents) == 0  # Should be suppressed by cooldown
