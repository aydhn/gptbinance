from typing import List
from app.research.regime.base import BaseRegimeEvaluator
from app.research.regime.enums import RegimeFamily, TrendRegime, ContextQuality
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)


class TrendPersistenceEvaluator(BaseRegimeEvaluator):
    @property
    def family(self) -> RegimeFamily:
        return RegimeFamily.TREND

    @property
    def required_features(self) -> List[str]:
        return ["trend_sma_fast", "trend_sma_slow", "momentum_rsi"]

    @property
    def min_history_required(self) -> int:
        return 10

    def evaluate(
        self, bundle: RegimeFeatureBundle, history: List[RegimeFeatureBundle] = None
    ) -> RegimeEvaluationResult:
        fast_sma = bundle.features.get("trend_sma_fast", 0.0)
        slow_sma = bundle.features.get("trend_sma_slow", 0.0)
        rsi = bundle.features.get("momentum_rsi", 50.0)

        # Basic logic for demonstration
        if fast_sma > slow_sma and rsi > 60:
            name = TrendRegime.STRONG_UPTREND.name
            score_val = 0.8
            rationale = "Fast SMA > Slow SMA and RSI > 60 indicating strong uptrend."
        elif fast_sma > slow_sma:
            name = TrendRegime.WEAK_UPTREND.name
            score_val = 0.5
            rationale = "Fast SMA > Slow SMA but RSI not confirming strong momentum."
        elif fast_sma < slow_sma and rsi < 40:
            name = TrendRegime.STRONG_DOWNTREND.name
            score_val = 0.8
            rationale = "Fast SMA < Slow SMA and RSI < 40 indicating strong downtrend."
        elif fast_sma < slow_sma:
            name = TrendRegime.WEAK_DOWNTREND.name
            score_val = 0.5
            rationale = "Fast SMA < Slow SMA but RSI not confirming strong momentum."
        else:
            name = TrendRegime.NO_TREND.name
            score_val = 0.2
            rationale = "Conflicting signals between SMA and RSI, no clear trend."

        label = RegimeLabel(family=self.family, name=name)
        score = RegimeScore(score=score_val, confidence=0.7)
        quality = RegimeQualityReport(
            quality=ContextQuality.MEDIUM, stability_score=0.5
        )

        return RegimeEvaluationResult(
            timestamp=bundle.timestamp,
            label=label,
            score=score,
            quality=quality,
            rationale=rationale,
            feature_contributions={
                "trend_sma_fast": fast_sma,
                "trend_sma_slow": slow_sma,
                "momentum_rsi": rsi,
            },
        )
