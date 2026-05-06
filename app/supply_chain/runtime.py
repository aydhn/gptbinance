from datetime import datetime, timezone
from app.supply_chain.models import RuntimeEquivalenceReport, BuildOutputManifest
from app.supply_chain.enums import RuntimeEquivalence


class RuntimeEquivalenceEvaluator:
    def evaluate(
        self, active_hash: str, expected_manifest: BuildOutputManifest
    ) -> RuntimeEquivalenceReport:
        is_equiv = active_hash == expected_manifest.hash

        return RuntimeEquivalenceReport(
            id=f"rteq_{expected_manifest.id}",
            runtime_surface_hash=active_hash,
            expected_build_id=expected_manifest.id,
            equivalence=RuntimeEquivalence.EQUIVALENT
            if is_equiv
            else RuntimeEquivalence.MISMATCH,
            mismatches=[]
            if is_equiv
            else ["Runtime active hash does not match expected build manifest hash."],
            timestamp=datetime.now(timezone.utc),
        )
