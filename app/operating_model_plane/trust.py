from app.operating_model_plane.models import OperatingModelObject, OperatingModelTrustVerdictReport
from app.operating_model_plane.enums import TrustVerdict, CoverageClass

class OperatingModelTrustEngine:
    def evaluate(self, obj: OperatingModelObject) -> OperatingModelTrustVerdictReport:
        breakdown = {}
        proof_notes = []

        ownerless = obj.is_critical and obj.primary_owner is None
        if ownerless:
            breakdown["ownership"] = "CRITICAL_OWNERLESS"
            proof_notes.append("Explicit blocker: Critical surface has no named owner.")
        else:
            breakdown["ownership"] = "ASSIGNED"

        missing_backup = obj.is_critical and obj.backup_coverage in [CoverageClass.BUSINESS_HOURS_ONLY, CoverageClass.NO_COVERAGE]
        if missing_backup:
            breakdown["coverage"] = "INSUFFICIENT"
            proof_notes.append("Explicit caution: Critical surface lacks 24/7 or follow-the-sun coverage.")
        else:
            breakdown["coverage"] = "SUFFICIENT"

        broken_escalation = obj.escalation_chain is None or obj.escalation_chain.is_broken
        if broken_escalation:
            breakdown["escalation"] = "BROKEN"
            proof_notes.append("Explicit debt: Escalation chain is missing or broken.")
        else:
            breakdown["escalation"] = "HEALTHY"

        if ownerless:
            verdict = TrustVerdict.BLOCKED
        elif missing_backup or broken_escalation:
            verdict = TrustVerdict.DEGRADED
        else:
            verdict = TrustVerdict.TRUSTED

        return OperatingModelTrustVerdictReport(
            verdict=verdict,
            breakdown=breakdown,
            stale_owner_debt=False,
            missing_backup_debt=missing_backup,
            broken_escalation_debt=broken_escalation,
            reviewer_conflict_debt=False,
            ownerless_critical_surface=ownerless,
            proof_notes=proof_notes
        )
