from typing import List
from app.research.regime.base import BaseRegimeEvaluator
from app.research.regime.enums import RegimeFamily, StructureRegime, ContextQuality
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)


class StructureBreakoutEvaluator(BaseRegimeEvaluator):
    @property
    def family(self) -> RegimeFamily:
        return RegimeFamily.STRUCTURE

    @property
    def required_features(self) -> List[str]:
        return ["close", "high", "low"]

    @property
    def min_history_required(self) -> int:
        return 10

    def evaluate(
        self, bundle: RegimeFeatureBundle, history: List[RegimeFeatureBundle] = None
    ) -> RegimeEvaluationResult:
        # Dummy structure evaluation since we lack complex pivot detection in features right now
        c = bundle.features.get("close", 100.0)
        h = bundle.features.get("high", 105.0)
        low_val = bundle.features.get("low", 95.0)

        # very naive logic for the sake of architecture
        if c > h * 0.99:
            name = StructureRegime.BREAKOUT_PRESSURE.name
            score_val = 0.7
            rationale = "Close is near local high, breakout pressure."
        else:
            name = StructureRegime.CONTINUATION.name
            score_val = 0.5
            rationale = "Normal structure continuation."

        label = RegimeLabel(family=self.family, name=name)
        score = RegimeScore(score=score_val, confidence=0.6)
        quality = RegimeQualityReport(
            quality=ContextQuality.MEDIUM, stability_score=0.5
        )

        return RegimeEvaluationResult(
            timestamp=bundle.timestamp,
            label=label,
            score=score,
            quality=quality,
            rationale=rationale,
            feature_contributions={"close": c, "high": h, "low": low_val},
        )
