from app.constitution_plane.models import ConstitutionTrustVerdict, FinalVerdictRecord
from app.constitution_plane.enums import TrustVerdict, VerdictClass

class TrustedConstitutionVerdictEngine:
    def evaluate(self, final_verdict: FinalVerdictRecord, stale_waivers: bool, hidden_overrides: bool) -> ConstitutionTrustVerdict:
        breakdown = {}
        caveats = []

        if hidden_overrides:
            trust_level = TrustVerdict.BLOCKED
            breakdown["overrides"] = "Hidden overrides detected. Cannot trust."
            caveats.append("Hidden override strictly prohibited.")
            return ConstitutionTrustVerdict(trust_level=trust_level, breakdown=breakdown, caveats=caveats)

        if stale_waivers:
            trust_level = TrustVerdict.DEGRADED
            breakdown["waivers"] = "Stale waivers detected."
            caveats.append("Stale waiver misuse warning.")
        elif final_verdict.final_verdict == VerdictClass.BLOCKED:
            trust_level = TrustVerdict.BLOCKED
            breakdown["verdict"] = "Blocked by final verdict."
        elif final_verdict.final_verdict == VerdictClass.REVIEW_REQUIRED:
            trust_level = TrustVerdict.REVIEW_REQUIRED
            breakdown["verdict"] = "Review required due to compound risk."
        elif final_verdict.final_verdict == VerdictClass.PASS_WITH_CAUTION:
            trust_level = TrustVerdict.CAUTION
            breakdown["verdict"] = "Pass with cautions."
        else:
            trust_level = TrustVerdict.TRUSTED
            breakdown["verdict"] = "Trusted."

        return ConstitutionTrustVerdict(trust_level=trust_level, breakdown=breakdown, caveats=caveats)
