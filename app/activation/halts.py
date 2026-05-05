from typing import List
from app.activation.models import HaltDecision, ProbationStatus, ActivationScope
from app.activation.enums import HaltSeverity, ProbationVerdict


class HaltEvaluator:
    CRITICAL_TRIGGERS = ["market_truth_health", "lifecycle_health"]

    @staticmethod
    def evaluate(
        probation_status: ProbationStatus, scope: ActivationScope
    ) -> HaltDecision:
        if probation_status.verdict == ProbationVerdict.FAIL:
            critical = any(
                b in HaltEvaluator.CRITICAL_TRIGGERS for b in probation_status.blockers
            )
            severity = (
                HaltSeverity.CRITICAL_IMMEDIATE if critical else HaltSeverity.CAUTION
            )
            return HaltDecision(
                intent_id=probation_status.intent_id,
                severity=severity,
                triggers=probation_status.blockers,
                affected_scopes=scope,
            )

        return HaltDecision(
            intent_id=probation_status.intent_id,
            severity=HaltSeverity.ADVISORY,
            triggers=[],
            affected_scopes=scope,
        )
