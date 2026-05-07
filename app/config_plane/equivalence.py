from app.config_plane.models import ConfigEquivalenceReport, EffectiveConfigManifest
from app.config_plane.enums import EquivalenceVerdict
from app.config_plane.diffs import ConfigDiffEngine


class EquivalenceChecker:
    def check_equivalence(
        self, candidate: EffectiveConfigManifest, runtime: EffectiveConfigManifest
    ) -> ConfigEquivalenceReport:
        diffs = ConfigDiffEngine().compare(candidate, runtime)
        verdict = EquivalenceVerdict.CLEAN if not diffs else EquivalenceVerdict.DEGRADED
        return ConfigEquivalenceReport(
            report_id="equiv_1",
            base_manifest_hash=candidate.config_hash,
            compare_manifest_hash=runtime.config_hash,
            verdict=verdict,
            divergences=diffs,
        )
