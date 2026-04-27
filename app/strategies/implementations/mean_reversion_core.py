from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategyContext,
    StrategyEvaluationResult,
    SignalCandidate,
    EntryIntentCandidate,
)
from app.strategies.enums import SignalDirection, SignalStatus
from app.strategies.rules import threshold_rule, band_rule
from app.strategies.scoring import ScoreBuilder


class MeanReversionCore(BaseStrategy):
    """
    Basic Mean Reversion Strategy.
    Hypothesis: If RSI is extreme and price is outside bands, it will revert.
    """

    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        result = StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )

        features = context.features
        rsi = features.get("rsi", 50.0)
        close = features.get("close", 0.0)
        upper = features.get("bollinger_upper", float("inf"))
        lower = features.get("bollinger_lower", 0.0)

        params = self.spec.parameters
        oversold = params.get("rsi_oversold", 30.0)
        overbought = params.get("rsi_overbought", 70.0)

        # Check RSI extremes
        is_oversold = threshold_rule(
            rsi, oversold, is_greater=False, name="RSI Oversold"
        )
        is_overbought = threshold_rule(
            rsi, overbought, is_greater=True, name="RSI Overbought"
        )

        if not (is_oversold.passed or is_overbought.passed):
            return result

        # Check Bands
        band_res = band_rule(close, upper, lower)

        direction = SignalDirection.NEUTRAL
        rationales = []

        if is_oversold.passed and "Below" in band_res.reason:
            direction = SignalDirection.LONG
            rationales = [is_oversold.to_rationale(), band_res.to_rationale()]
        elif is_overbought.passed and "Above" in band_res.reason:
            direction = SignalDirection.SHORT
            rationales = [is_overbought.to_rationale(), band_res.to_rationale()]

        if direction == SignalDirection.NEUTRAL:
            return result

        score_builder = ScoreBuilder(base_score=60.0)
        for r in rationales:
            score_builder.add_component(r.category.value, 10.0, r.reason)

        final_score = score_builder.build(confidence=0.7, quality=0.8)

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

        if final_score.value >= 75.0:
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
