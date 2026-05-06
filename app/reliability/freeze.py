import uuid
from typing import List, Optional
from app.reliability.enums import FreezeClass, ScorecardVerdict
from app.reliability.models import FreezeRecommendation, HealthScorecard, BurnRateReport


class ChangeFreezeRecommendationEngine:
    @staticmethod
    def evaluate(
        scorecards: List[HealthScorecard], burn_reports: List[BurnRateReport]
    ) -> List[FreezeRecommendation]:
        recommendations = []

        # Check for blocked scorecards which might warrant an expansion hold
        blocked_domains = [
            s.domain.value for s in scorecards if s.verdict == ScorecardVerdict.BLOCKED
        ]
        if blocked_domains:
            recommendations.append(
                FreezeRecommendation(
                    recommendation_id=f"freeze_{uuid.uuid4().hex[:8]}",
                    freeze_class=FreezeClass.NO_EXPANSION_RECOMMENDED,
                    scope="global_expansion",
                    rationale=f"Domains are currently blocked: {', '.join(blocked_domains)}.",
                    budget_evidence_refs=[
                        s.scorecard_id
                        for s in scorecards
                        if s.verdict == ScorecardVerdict.BLOCKED
                    ],
                )
            )

            recommendations.append(
                FreezeRecommendation(
                    recommendation_id=f"freeze_{uuid.uuid4().hex[:8]}",
                    freeze_class=FreezeClass.RELEASE_HOLD_RECOMMENDED,
                    scope="production_releases",
                    rationale=f"Release hold recommended due to blocked domains: {', '.join(blocked_domains)}.",
                )
            )

        # Check for fast burn
        fast_burns = [br for br in burn_reports if br.severity == "fast_burn"]
        if fast_burns:
            recommendations.append(
                FreezeRecommendation(
                    recommendation_id=f"freeze_{uuid.uuid4().hex[:8]}",
                    freeze_class=FreezeClass.MAJOR_CHANGE_FREEZE,
                    scope="system_wide",
                    rationale=f"Fast burn detected on {len(fast_burns)} budgets.",
                    budget_evidence_refs=[br.report_id for br in fast_burns],
                )
            )

        # Check specific domains
        for s in scorecards:
            if s.domain.value == "activation_probation" and s.verdict in [
                ScorecardVerdict.DEGRADED,
                ScorecardVerdict.BLOCKED,
            ]:
                recommendations.append(
                    FreezeRecommendation(
                        recommendation_id=f"freeze_{uuid.uuid4().hex[:8]}",
                        freeze_class=FreezeClass.NO_NEW_CANDIDATE_ACTIVATION,
                        scope="candidate_activation",
                        rationale=f"Activation probation health is {s.verdict.value}.",
                        budget_evidence_refs=[s.scorecard_id],
                    )
                )

        return recommendations
