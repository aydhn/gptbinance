from typing import Optional
from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategyEvaluationResult,
    SignalCandidate,
    StrategyScore,
)
from app.strategies.enums import SignalDirection, SignalStatus


class MockStrategy(BaseStrategy):
    def _evaluate_impl(self, context) -> StrategyEvaluationResult:
        # Just generate a buy signal every time to test the flow
        signal = SignalCandidate(
            strategy_name=self.spec.name,
            symbol=context.symbol,
            interval=context.interval,
            timestamp=context.timestamp,
            direction=SignalDirection.LONG,
            status=SignalStatus.ACCEPTED,
            score=StrategyScore(value=1.0, confidence=1.0, quality=1.0),
        )
        return StrategyEvaluationResult(
            strategy_name=self.spec.name,
            symbol=context.symbol,
            timestamp=context.timestamp,
            signal=signal,
            is_active=True,
        )
