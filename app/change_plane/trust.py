from datetime import datetime, timezone
from app.change_plane.models import ChangeObject, ChangeTrustVerdictModel as TrustVerdictModel
from app.change_plane.enums import ChangeTrustVerdict, ApprovalClass, ExecutionClass, VerificationClass, WindowClass

class ChangeTrustEngine:
    def evaluate(self, change: ChangeObject) -> TrustVerdictModel:
        factors = {}
        verdict = ChangeTrustVerdict.TRUSTED

        if not getattr(change, "request", None) or not getattr(change, "impact", None):
            factors["intent_impact"] = "Missing request or impact assessment"
            verdict = ChangeTrustVerdict.BLOCKED

        br = getattr(change, "blast_radius", None)
        if br and br.unknown_radius_warnings:
            factors["blast_radius"] = "Unknown blast radius warnings present"
            if verdict in [ChangeTrustVerdict.TRUSTED, ChangeTrustVerdict.REVIEW_REQUIRED]:
                verdict = ChangeTrustVerdict.CAUTION

        appr = getattr(change, "approval", None)
        if not appr or not getattr(appr, "approved_at", None):
            factors["approval"] = "Missing or unapproved chain"
            verdict = ChangeTrustVerdict.BLOCKED
        elif appr.approval_class == ApprovalClass.EMERGENCY_APPROVAL:
            factors["approval"] = "Emergency approval requires review"
            if verdict == ChangeTrustVerdict.TRUSTED:
                verdict = ChangeTrustVerdict.REVIEW_REQUIRED

        if not getattr(change, "window", None):
            factors["window"] = "Unscheduled change"
            verdict = ChangeTrustVerdict.BLOCKED

        rb = getattr(change, "rollback", None)
        if not rb or rb.feasibility == "Low":
            factors["rollback"] = "Weak rollback readiness"
            if verdict in [ChangeTrustVerdict.TRUSTED, ChangeTrustVerdict.REVIEW_REQUIRED]:
                verdict = ChangeTrustVerdict.CAUTION

        verf = getattr(change, "verification", None)
        if not verf or verf.verification_class == VerificationClass.UNVERIFIED:
            factors["verification"] = "Unverified safe-change claim"
            if verdict in [ChangeTrustVerdict.TRUSTED, ChangeTrustVerdict.REVIEW_REQUIRED]:
                verdict = ChangeTrustVerdict.CAUTION

        return TrustVerdictModel(
            change_id=change.change_id,
            verdict=verdict,
            factors=factors,
            breakdown_mandatory=True,
            generated_at=datetime.now(timezone.utc)
        )
