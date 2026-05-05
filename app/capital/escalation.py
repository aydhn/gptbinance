from datetime import datetime, timezone
import uuid
from typing import Dict, Any, List

from app.capital.models import (
    CapitalEscalationCheck,
    CapitalReadinessReport,
    CapitalEvidenceBundle,
)
from app.capital.enums import EscalationVerdict, EvidenceFreshness
from app.capital.base import EscalationEvaluatorBase
from app.capital.tiers import get_tier
from app.capital.ladder import is_transition_allowed, get_next_logical_tier
from app.capital.evidence import check_required_evidence
from app.policy_kernel.enums import PolicyDomain, PolicyVerdict


class StrictEscalationEvaluator(EscalationEvaluatorBase):
    def check_escalation_readiness(
        self,
        current_tier_id: str,
        target_tier_id: str,
        evidence_bundle: CapitalEvidenceBundle,
    ) -> CapitalEscalationCheck:
        blockers = []
        warnings = []

        if not is_transition_allowed(current_tier_id, target_tier_id):
            blockers.append(
                f"Transition from {current_tier_id} to {target_tier_id} is not allowed by the ladder."
            )

        target_tier = None
        try:
            target_tier = get_tier(target_tier_id)
        except Exception:
            blockers.append(f"Target tier {target_tier_id} does not exist.")

        if target_tier:
            missing = check_required_evidence(
                evidence_bundle, target_tier.required_evidence_types
            )
            if missing:
                blockers.append(
                    f"Missing required evidence for {target_tier_id}: {', '.join(missing)}"
                )

            if evidence_bundle.freshness == EvidenceFreshness.STALE:
                blockers.append(
                    "Evidence bundle contains stale data. Fresh evidence required for escalation."
                )

        verdict = EscalationVerdict.PASS
        if blockers:
            verdict = EscalationVerdict.BLOCKED
        elif warnings:
            verdict = EscalationVerdict.CAUTION

        report = CapitalReadinessReport(
            is_ready=(verdict == EscalationVerdict.PASS),
            verdict=verdict,
            blockers=blockers,
            warnings=warnings,
            next_tier_recommendation=get_next_logical_tier(current_tier_id),
        )

        return CapitalEscalationCheck(
            check_id=f"esc_{uuid.uuid4().hex[:8]}",
            timestamp=datetime.now(timezone.utc),
            current_tier_id=current_tier_id,
            target_tier_id=target_tier_id,
            readiness=report,
        )

    def get_policy_domain_outputs(
        self, check: CapitalEscalationCheck
    ) -> Dict[str, Any]:
        """Expose Capital Escalation outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        if check.readiness.verdict == EscalationVerdict.BLOCKED:
            verdict = PolicyVerdict.BLOCK
        elif check.readiness.verdict == EscalationVerdict.CAUTION:
            verdict = PolicyVerdict.CAUTION

        return {
            "domain": PolicyDomain.CAPITAL,
            "reasons": check.readiness.blockers + check.readiness.warnings,
            "verdict": verdict,
            "is_ready": check.readiness.is_ready,
        }


escalation_engine = StrictEscalationEvaluator()
