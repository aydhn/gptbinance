from datetime import datetime, timezone
from app.supply_chain.models import (
    TrustedArtifactVerdict,
    LockIntegrityRecord,
    ReproducibilityResult,
    RuntimeEquivalenceReport,
)
from app.supply_chain.enums import (
    TrustVerdict,
    IntegrityVerdict,
    ReproducibilityClass,
    RuntimeEquivalence,
)


class TrustVerdictEngine:
    def evaluate(
        self,
        artifact_id: str,
        lock_rec: LockIntegrityRecord,
        repro_res: ReproducibilityResult,
        run_eq: RuntimeEquivalenceReport,
        has_attestation: bool,
    ) -> TrustedArtifactVerdict:
        factors = {}
        verdict = TrustVerdict.TRUSTED

        if lock_rec.verdict != IntegrityVerdict.VERIFIED:
            verdict = TrustVerdict.DEGRADED
            factors["lock_integrity"] = "Broken"
        else:
            factors["lock_integrity"] = "Verified"

        if (
            repro_res
            and repro_res.reproducibility_class != ReproducibilityClass.DETERMINISTIC
        ):
            verdict = (
                TrustVerdict.CAUTION if verdict == TrustVerdict.TRUSTED else verdict
            )
            factors["reproducibility"] = "Non-deterministic"
        else:
            factors["reproducibility"] = "Deterministic"

        if run_eq and run_eq.equivalence != RuntimeEquivalence.EQUIVALENT:
            verdict = TrustVerdict.BLOCKED
            factors["runtime_equivalence"] = "Mismatch"
        else:
            factors["runtime_equivalence"] = "Equivalent"

        if not has_attestation:
            verdict = (
                TrustVerdict.REVIEW_REQUIRED
                if verdict in [TrustVerdict.TRUSTED, TrustVerdict.CAUTION]
                else verdict
            )
            factors["attestation"] = "Missing"
        else:
            factors["attestation"] = "Present"

        return TrustedArtifactVerdict(
            artifact_id=artifact_id,
            verdict=verdict,
            factors=factors,
            timestamp=datetime.now(timezone.utc),
        )
