import json
from app.config_plane.models import EffectiveConfigManifest, ConfigEquivalenceReport
from app.config_plane.secrets import get_redacted_manifest

def summarize_effective_config(manifest: EffectiveConfigManifest, redacted: bool = True) -> str:
    data = get_redacted_manifest(manifest) if redacted else manifest.model_dump()
    return json.dumps({
        "manifest_id": data["manifest_id"],
        "profile": data["profile"],
        "config_hash": data["config_hash"],
        "entry_count": len(data["entries"])
    }, indent=2)

def generate_equivalence_summary(report: ConfigEquivalenceReport) -> str:
    return f"Equivalence Verdict: {report.verdict.value.upper()} | Divergences: {len(report.divergences)}"
