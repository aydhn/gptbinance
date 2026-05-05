from app.experiments.base import ComparisonEvaluatorBase
from app.experiments.enums import ComparisonVerdict, EvidenceConfidence


class BaselineComparisonEvaluator(ComparisonEvaluatorBase):
    def evaluate(self, run_id: str) -> dict:
        # Dummy evaluation logic
        return {
            "comparison_id": "comp_123",
            "run_id": run_id,
            "baseline_arm_id": "arm_baseline",
            "candidate_arm_id": "arm_candidate",
            "verdict": ComparisonVerdict.IMPROVEMENT.value,
            "confidence": EvidenceConfidence.MEDIUM.value,
            "metrics_delta": {"pnl": 0.05, "friction": -0.1},
            "caveats": ["Sample size is somewhat small"],
        }
