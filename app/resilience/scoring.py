from app.resilience.base import BaseResilienceScorer
from app.resilience.models import ExperimentSummary, ResilienceScore
from app.resilience.enums import AssertionVerdict


class ResilienceScorer(BaseResilienceScorer):
    def calculate_score(self, summary: ExperimentSummary) -> ResilienceScore:
        total_assertions = len(summary.assertion_results) + len(
            summary.recovery_results
        )
        passed_assertions = sum(
            1
            for a in summary.assertion_results + summary.recovery_results
            if a.verdict == AssertionVerdict.PASS
        )

        pass_rate = (
            (passed_assertions / total_assertions) if total_assertions > 0 else 0.0
        )

        # Simplified scoring logic for demonstration
        detection_score = 100 if pass_rate > 0.8 else 50
        containment_score = 100 if pass_rate > 0.8 else 50
        recovery_score = (
            100
            if sum(
                1
                for a in summary.recovery_results
                if a.verdict == AssertionVerdict.PASS
            )
            == len(summary.recovery_results)
            and len(summary.recovery_results) > 0
            else 50
        )

        if total_assertions == 0:
            overall_score = 0
            detection_score = 0
            containment_score = 0
            recovery_score = 0
        else:
            overall_score = int(
                (detection_score + containment_score + recovery_score) / 3 * pass_rate
            )

        return ResilienceScore(
            overall_score=overall_score,
            detection_score=detection_score,
            containment_score=containment_score,
            recovery_score=recovery_score,
            assertions_pass_rate=pass_rate,
        )
