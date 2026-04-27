from typing import List
from app.research.regime.base import BaseRegimeEvaluator
from app.research.regime.enums import RegimeFamily, ContextQuality
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)


class MeanReversionProneEvaluator(BaseRegimeEvaluator):
    @property
    def family(self) -> RegimeFamily:
        return RegimeFamily.MEAN_REVERSION

    @property
    def required_features(self) -> List[str]:
        return ["momentum_rsi", "price_to_sma_dist"]

    @property
    def min_history_required(self) -> int:
        return 10

    def evaluate(
        self, bundle: RegimeFeatureBundle, history: List[RegimeFeatureBundle] = None
    ) -> RegimeEvaluationResult:
        rsi = bundle.features.get("momentum_rsi", 50.0)
        dist = bundle.features.get("price_to_sma_dist", 0.0)

        # Simple logic
        if rsi > 75 or rsi < 25 or abs(dist) > 0.05:
            name = "OVERSTRETCHED"
            score_val = 0.8
            rationale = "RSI extreme or high distance from SMA, prone to snap back."
        elif 40 < rsi < 60 and abs(dist) < 0.01:
            name = "RANGE_BOUND"
            score_val = 0.7
            rationale = "RSI neutral and close to SMA, typical range-bound chop."
        else:
            name = "OSCILLATORY"
            score_val = 0.5
            rationale = "Normal oscillations without extremes."

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
            feature_contributions={"momentum_rsi": rsi, "price_to_sma_dist": dist},
        )
