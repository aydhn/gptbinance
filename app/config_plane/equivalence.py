from typing import List
import uuid
from app.config_plane.models import EffectiveConfigManifest, ConfigEquivalenceReport
from app.config_plane.enums import EquivalenceVerdict
from app.config_plane.diffs import calculate_diff
from datetime import datetime, timezone


def evaluate_equivalence(
    baseline: EffectiveConfigManifest, target: EffectiveConfigManifest
) -> ConfigEquivalenceReport:
    diffs = calculate_diff(baseline, target)

    if not diffs:
        verdict = EquivalenceVerdict.CLEAN
    else:
        verdict = EquivalenceVerdict.DEGRADED  # Simplified logic

    divergences = [
        f"{d.parameter_ref.domain.value}.{d.parameter_ref.name}" for d in diffs
    ]

    return ConfigEquivalenceReport(
        report_id=f"eq_{uuid.uuid4().hex[:8]}",
        target_manifest_id=target.manifest_id,
        baseline_manifest_id=baseline.manifest_id,
        verdict=verdict,
        divergences=divergences,
        evaluated_at=datetime.now(timezone.utc),
    )
