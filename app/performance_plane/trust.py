import uuid
from typing import List
from app.performance_plane.models import PerformanceTrustVerdict, PerformanceManifest
from app.performance_plane.enums import TrustVerdict


class TrustEngine:
    @staticmethod
    def evaluate(
        manifest: PerformanceManifest, quality_warnings: List[str]
    ) -> PerformanceTrustVerdict:
        verdict = TrustVerdict.TRUSTED
        blockers = []

        if not manifest.window.is_complete:
            verdict = TrustVerdict.CAUTION
            blockers.append("Incomplete window.")

        if len(quality_warnings) > 0:
            verdict = TrustVerdict.DEGRADED
            blockers.extend(quality_warnings)

        return PerformanceTrustVerdict(
            verdict_id=str(uuid.uuid4()),
            manifest_id=manifest.manifest_id,
            verdict=verdict,
            blockers=blockers,
            factors={"warning_count": len(quality_warnings)},
        )
