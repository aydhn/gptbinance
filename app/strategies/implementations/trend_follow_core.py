from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategyContext,
    StrategyEvaluationResult,
    SignalCandidate,
    EntryIntentCandidate,
)
from app.strategies.enums import SignalDirection, SignalStatus
from app.strategies.rules import crossover_rule
from app.strategies.scoring import ScoreBuilder


class TrendFollowCore(BaseStrategy):
    """
    Basic Trend Following Strategy.
    Hypothesis: If fast SMA crosses slow SMA and slope is positive, trend will continue.
    """

    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        result = StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )

        features = context.features

        # In a real scenario, we'd have historical buffers. We'll simulate previous values for the example if missing.
        fast = features.get("sma_fast", 0.0)
        slow = features.get("sma_slow", 0.0)
        prev_fast = features.get("prev_sma_fast", fast * 0.99)  # Mock previous
        prev_slow = features.get("prev_sma_slow", slow * 1.01)  # Mock previous

        # Rules
        cross = crossover_rule(fast, slow, prev_fast, prev_slow)

        if not cross.passed:
            return result

        direction = (
            SignalDirection.LONG if "Bullish" in cross.reason else SignalDirection.SHORT
        )

        # Scoring
        score_builder = ScoreBuilder(base_score=50.0)
        score_builder.add_component("Crossover", 20.0, cross.reason)

        # Volatility check (optional modifier)
        atr = features.get("atr", 0.0)
        if atr > 0:
            score_builder.add_component("Volatility", 10.0, f"ATR is {atr:.2f}")

        final_score = score_builder.build(confidence=0.8, quality=0.9)

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

        # Generate Intent if score is high enough
        if final_score.value >= 70.0:
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
