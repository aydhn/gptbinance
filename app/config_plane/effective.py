from app.config_plane.models import EffectiveConfigManifest


# Helpers for immutable manifest operations
def serialize_manifest(manifest: EffectiveConfigManifest) -> dict:
    return manifest.model_dump(mode="json")


def deserialize_manifest(data: dict) -> EffectiveConfigManifest:
    return EffectiveConfigManifest.model_validate(data)
