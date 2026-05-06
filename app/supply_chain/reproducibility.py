from datetime import datetime, timezone
from app.supply_chain.models import (
    ReproducibilityRun,
    ReproducibilityResult,
    BuildOutputManifest,
)
from app.supply_chain.enums import ReproducibilityClass


class ReproducibilityChecker:
    def check(
        self,
        original_manifest: BuildOutputManifest,
        rebuild_manifest: BuildOutputManifest,
    ) -> ReproducibilityRun:
        is_reproducible = original_manifest.hash == rebuild_manifest.hash

        diffs = []
        if not is_reproducible:
            diffs.append("Manifest hashes differ")

        result = ReproducibilityResult(
            build_id=original_manifest.id,
            reproducibility_class=ReproducibilityClass.DETERMINISTIC
            if is_reproducible
            else ReproducibilityClass.NON_DETERMINISTIC,
            diff_surfaces=diffs,
            timestamp=datetime.now(timezone.utc),
        )

        return ReproducibilityRun(
            id=f"rep_{original_manifest.id}",
            original_build_id=original_manifest.id,
            rebuild_manifest_id=rebuild_manifest.id,
            result=result,
        )
