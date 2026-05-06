import uuid
from typing import List
from app.reliability.enums import OperationalReviewClass, ScorecardVerdict
from app.reliability.models import HoldRecommendation, HealthScorecard


class OperationalHoldRecommendationEngine:
    @staticmethod
    def evaluate(scorecards: List[HealthScorecard]) -> List[HoldRecommendation]:
        holds = []

        for s in scorecards:
            if (
                s.domain.value == "release_readiness_health"
                and s.verdict == ScorecardVerdict.REVIEW_REQUIRED
            ):
                holds.append(
                    HoldRecommendation(
                        hold_id=f"hold_{uuid.uuid4().hex[:8]}",
                        hold_class=OperationalReviewClass.BOARD_REVIEW_HOLD,
                        scope="readiness_board",
                        rationale="Board review required due to stale or incomplete evidence.",
                        expiry_conditions=["evidence_refresh", "manual_override"],
                    )
                )

            if (
                s.domain.value == "remediation_closure"
                and s.verdict == ScorecardVerdict.BLOCKED
            ):
                holds.append(
                    HoldRecommendation(
                        hold_id=f"hold_{uuid.uuid4().hex[:8]}",
                        hold_class=OperationalReviewClass.REMEDIATION_ONLY_MODE,
                        scope="global",
                        rationale="Remediation debt has blocked normal operations. Remediation-only mode advised.",
                        expiry_conditions=["debt_reduced_below_critical"],
                    )
                )

            if (
                s.domain.value == "migration_stability"
                and s.verdict == ScorecardVerdict.DEGRADED
            ):
                holds.append(
                    HoldRecommendation(
                        hold_id=f"hold_{uuid.uuid4().hex[:8]}",
                        hold_class=OperationalReviewClass.MIGRATION_APPLY_HOLD,
                        scope="migrations",
                        rationale="Migration stability degraded. Hold new migrations.",
                        expiry_conditions=["verification_pass"],
                    )
                )

        return holds
