from typing import List
from app.research.regime.base import BaseRegimeEvaluator
from app.research.regime.enums import RegimeFamily, VolatilityRegime, ContextQuality
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)


class VolatilityExpansionEvaluator(BaseRegimeEvaluator):
    @property
    def family(self) -> RegimeFamily:
        return RegimeFamily.VOLATILITY

    @property
    def required_features(self) -> List[str]:
        return ["volatility_atr", "volatility_bb_width"]

    @property
    def min_history_required(self) -> int:
        return 10

    def evaluate(
        self, bundle: RegimeFeatureBundle, history: List[RegimeFeatureBundle] = None
    ) -> RegimeEvaluationResult:
        atr = bundle.features.get("volatility_atr", 1.0)
        bb_width = bundle.features.get("volatility_bb_width", 1.0)

        # Simple thresholding logic for demonstration
        if atr > 2.0 and bb_width > 2.0:
            name = VolatilityRegime.NOISY_HIGH_VOL.name
            score_val = 0.9
            rationale = "ATR and BB Width are very high, indicating extreme volatility."
        elif atr > 1.5 or bb_width > 1.5:
            name = VolatilityRegime.EXPANSION.name
            score_val = 0.7
            rationale = "Volatility is expanding as ATR or BB width is elevated."
        elif atr < 0.5 and bb_width < 0.5:
            name = VolatilityRegime.LOW_ENERGY.name
            score_val = 0.8
            rationale = "ATR and BB Width are very low, market is in low energy state."
        else:
            name = VolatilityRegime.NORMAL.name
            score_val = 0.5
            rationale = "Volatility metrics are within normal ranges."

        label = RegimeLabel(family=self.family, name=name)
        score = RegimeScore(score=score_val, confidence=0.8)
        quality = RegimeQualityReport(quality=ContextQuality.HIGH, stability_score=0.6)

        return RegimeEvaluationResult(
            timestamp=bundle.timestamp,
            label=label,
            score=score,
            quality=quality,
            rationale=rationale,
            feature_contributions={
                "volatility_atr": atr,
                "volatility_bb_width": bb_width,
            },
        )
