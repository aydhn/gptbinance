from app.config_plane.models import EffectiveConfigManifest
from app.config_plane.enums import ParameterClass


def get_redacted_manifest(manifest: EffectiveConfigManifest) -> dict:
    """Returns a dict representation where secret values are heavily redacted"""
    data = manifest.model_dump()
    for key, entry in data["entries"].items():
        # Actually our resolution logic puts REDACTED in lineage, but let's ensure the main value is hidden too
        if entry["lineage"]["secret_redacted"]:
            entry["value"] = "******"
    return data
