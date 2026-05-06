from typing import List
from app.activation.models import HaltDecision, ProbationStatus, ActivationScope
from app.activation.enums import HaltSeverity, ProbationVerdict
from app.incidents.intake import IncidentCommand
from app.incidents.signals import SignalMapper
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
import uuid


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

            # Export to incident command
            cmd = IncidentCommand()
            sig = SignalMapper.create_signal(
                signal_id=f"halt-{uuid.uuid4().hex[:8]}",
                signal_type=SignalType.ACTIVATION_PROBATION_FAIL,
                domain="activation",
                scope_type=IncidentScopeType.PROFILE if scope.profile_id else IncidentScopeType.GLOBAL,
                scope_ref=scope.profile_id if scope.profile_id else "GLOBAL",
                severity=IncidentSeverity.CRITICAL_INCIDENT if critical else IncidentSeverity.MAJOR_INCIDENT,
                details={"intent_id": probation_status.intent_id, "triggers": probation_status.blockers}
            )
            cmd.ingest_signal(sig)

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


# Exported signals to incident command: Probation failures -> Incident Intake

# Exported signals to incident command: Probation failures -> Incident Intake