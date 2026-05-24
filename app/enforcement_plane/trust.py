from app.enforcement_plane.models import EnforcementObject, EnforcementTrustVerdict
from app.enforcement_plane.enums import TrustVerdictClass, AppealClass

class TrustedEnforcementVerdictEngine:
    def evaluate(self, enforcement: EnforcementObject) -> EnforcementTrustVerdict:
        verdict = TrustVerdictClass.TRUSTED
        blockers = []
        warnings = []
        factors = {}

        # 1. Indefinite Hold Check
        if not enforcement.expiry_at and not enforcement.lift_criteria:
            verdict = TrustVerdictClass.BLOCKED
            blockers.append("Indefinite Hold Detected: No expiry or lift criteria provided.")

        # 2. Due Process Check
        if enforcement.appeal_posture == AppealClass.DUE_PROCESS_BYPASSED:
            if verdict == TrustVerdictClass.TRUSTED:
                verdict = TrustVerdictClass.DEGRADED
            warnings.append("Due Process Bypass: Shadow enforcement or coercive action lacking appeal path.")

        # 3. Trigger & Scope
        factors["trigger_basis"] = "Verified" if enforcement.trigger.is_authoritative else "Weak Evidence"
        if not enforcement.trigger.is_authoritative:
            warnings.append("Caution: Enforcement relies on weak evidence.")
            if verdict == TrustVerdictClass.TRUSTED: verdict = TrustVerdictClass.CAUTION

        return EnforcementTrustVerdict(
            enforcement_id=enforcement.enforcement_id,
            verdict=verdict,
            factors=factors,
            debt_warnings=warnings,
            blockers=blockers
        )
