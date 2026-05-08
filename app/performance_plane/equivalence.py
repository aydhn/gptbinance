import uuid
from typing import List
from app.performance_plane.models import (
    PerformanceEquivalenceReport,
    PerformanceManifest,
)
from app.performance_plane.enums import EquivalenceVerdict


class EquivalenceChecker:
    @staticmethod
    def check(
        source: PerformanceManifest, target: PerformanceManifest
    ) -> PerformanceEquivalenceReport:
        verdict = EquivalenceVerdict.EQUIVALENT
        divergences = []

        if source.window.start_time != target.window.start_time:
            verdict = EquivalenceVerdict.NOT_COMPARABLE
            divergences.append("Window start times do not match.")

        if source.hash_signature != target.hash_signature:
            # Simplified logic, in reality we'd compare attribution nodes, returns, etc.
            if verdict == EquivalenceVerdict.EQUIVALENT:
                verdict = EquivalenceVerdict.MINOR_DIVERGENCE
                divergences.append("Manifest hash signatures differ.")

        return PerformanceEquivalenceReport(
            report_id=str(uuid.uuid4()),
            source_manifest_id=source.manifest_id,
            target_manifest_id=target.manifest_id,
            verdict=verdict,
            divergence_sources=divergences,
        )
