from app.experiments.base import PromotionEvaluatorBase
from app.experiments.enums import PromotionClass, ComparisonVerdict


class CandidatePromotionEvaluator(PromotionEvaluatorBase):
    def evaluate(self, comparison_results: dict, fragility_results: dict) -> str:
        verdict = comparison_results.get("verdict")
        if verdict == ComparisonVerdict.IMPROVEMENT.value:
            if fragility_results.get("overfit_suspicion"):
                return PromotionClass.KEEP_RESEARCHING.value
            return PromotionClass.QUALIFIES_FOR_PAPER_SHADOW.value
        return PromotionClass.REJECT.value
