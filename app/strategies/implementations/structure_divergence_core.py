from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategyContext,
    StrategyEvaluationResult,
    SignalCandidate,
    EntryIntentCandidate,
)
from app.strategies.enums import SignalDirection, SignalStatus
from app.strategies.scoring import ScoreBuilder


class StructureDivergenceCore(BaseStrategy):
    """
    Basic Structure/Divergence Strategy.
    Hypothesis: If price makes HH but oscillator makes LH, bearish divergence (and vice versa).
    """

    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        result = StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )

        # Very simplified mock divergence check
        features = context.features

        # In reality, this requires checking historical pivot points and oscillator values at those points
        has_bullish_div = features.get("mock_bullish_div", False)
        has_bearish_div = features.get("mock_bearish_div", False)

        if not (has_bullish_div or has_bearish_div):
            return result

        direction = SignalDirection.LONG if has_bullish_div else SignalDirection.SHORT

        score_builder = ScoreBuilder(base_score=80.0)
        score_builder.add_component("Divergence", 10.0, "Divergence pattern detected")

        final_score = score_builder.build(confidence=0.9, quality=0.9)

        signal = SignalCandidate(
            strategy_name=self.name,
            symbol=context.symbol,
            interval=context.interval,
            timestamp=context.timestamp,
            direction=direction,
            status=SignalStatus.ACCEPTED,
            score=final_score,
            rationale=score_builder.rationales,
        )
        result.signal = signal

        result.entry_intent = EntryIntentCandidate(
            strategy_name=self.name,
            symbol=context.symbol,
            timestamp=context.timestamp,
            direction=direction,
            score=final_score.value,
            confidence=final_score.confidence,
            rationale=score_builder.rationales,
        )

        return result
