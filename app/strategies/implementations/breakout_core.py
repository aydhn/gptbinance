from app.strategies.base import BaseStrategy
from app.strategies.models import (
    StrategyContext,
    StrategyEvaluationResult,
    SignalCandidate,
    EntryIntentCandidate,
)
from app.strategies.enums import SignalDirection, SignalStatus
from app.strategies.rules import threshold_rule
from app.strategies.scoring import ScoreBuilder


class BreakoutCore(BaseStrategy):
    """
    Basic Breakout Strategy.
    Hypothesis: If price breaks range with high volume, breakout will continue.
    """

    def evaluate(self, context: StrategyContext) -> StrategyEvaluationResult:
        result = StrategyEvaluationResult(
            strategy_name=self.name, symbol=context.symbol, timestamp=context.timestamp
        )

        features = context.features
        close = features.get("close", 0.0)
        upper = features.get("donchian_upper", float("inf"))
        lower = features.get("donchian_lower", 0.0)
        vol = features.get("volume", 0.0)
        vol_sma = features.get("volume_sma", 1.0)

        vol_mult = self.spec.parameters.get("volume_multiplier", 1.5)

        break_up = threshold_rule(close, upper, is_greater=True, name="Upper Breakout")
        break_down = threshold_rule(
            close, lower, is_greater=False, name="Lower Breakout"
        )

        if not (break_up.passed or break_down.passed):
            return result

        vol_confirm = threshold_rule(
            vol, vol_sma * vol_mult, is_greater=True, name="Volume Confirmation"
        )

        direction = SignalDirection.LONG if break_up.passed else SignalDirection.SHORT

        score_builder = ScoreBuilder(base_score=40.0)
        score_builder.add_component(
            "Breakout", 30.0, break_up.reason if break_up.passed else break_down.reason
        )

        if vol_confirm.passed:
            score_builder.add_component("Volume", 20.0, vol_confirm.reason)
        else:
            score_builder.add_component(
                "Low Volume", -10.0, vol_confirm.reason, is_penalty=True
            )

        final_score = score_builder.build(confidence=0.6, quality=0.7)

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
