from app.execution_plane.models import TrustedExecutionVerdict
from app.execution_plane.enums import TrustedExecutionVerdictClass


class TrustVerdictEngine:
    @staticmethod
    def evaluate(
        manifest_id: str,
        preflight_blockers: list,
        equivalence_verdict: str,
        quality_score: int,
    ) -> TrustedExecutionVerdict:
        verdict = TrustedExecutionVerdictClass.TRUSTED
        breakdown = []

        if preflight_blockers:
            verdict = TrustedExecutionVerdictClass.BLOCKED
            breakdown.append(f"Preflight blockers present: {preflight_blockers}")

        if equivalence_verdict == "blocked":
            verdict = TrustedExecutionVerdictClass.BLOCKED
            breakdown.append("Equivalence severely broken.")
        elif equivalence_verdict == "degraded":
            if verdict != TrustedExecutionVerdictClass.BLOCKED:
                verdict = TrustedExecutionVerdictClass.DEGRADED
                breakdown.append("Equivalence degraded.")

        if quality_score < 50:
            if verdict not in [
                TrustedExecutionVerdictClass.BLOCKED,
                TrustedExecutionVerdictClass.DEGRADED,
            ]:
                verdict = TrustedExecutionVerdictClass.CAUTION
            breakdown.append(f"Low quality score: {quality_score}")

        if verdict == TrustedExecutionVerdictClass.TRUSTED:
            breakdown.append("All checks passed.")

        return TrustedExecutionVerdict(
            manifest_id=manifest_id,
            verdict=verdict,
            factors={"equivalence": equivalence_verdict, "quality": str(quality_score)},
            breakdown=breakdown,
        )
