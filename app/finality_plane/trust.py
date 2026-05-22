from app.finality_plane.enums import FinalityTrustVerdictClass
from app.finality_plane.models import FinalityTrustVerdict

class FinalityTrustEngine:
    @staticmethod
    def evaluate_trust(finality_id: str, closure_basis_strength: str, reopen_clarity: str,
                       settlement_rigor: str, residual_duty_visibility: str,
                       caveats: list, blockers: list) -> FinalityTrustVerdict:

        verdict = FinalityTrustVerdictClass.TRUSTED
        if blockers:
            verdict = FinalityTrustVerdictClass.BLOCKED
        elif "premature" in closure_basis_strength.lower() or "unclear" in reopen_clarity.lower():
            verdict = FinalityTrustVerdictClass.CAUTION

        return FinalityTrustVerdict(
            verdict=verdict,
            finality_id=finality_id,
            closure_basis_strength=closure_basis_strength,
            reopen_clarity=reopen_clarity,
            settlement_rigor=settlement_rigor,
            residual_duty_visibility=residual_duty_visibility,
            caveats=caveats,
            blockers=blockers
        )
