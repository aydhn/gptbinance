from app.waterfall_plane.models import WaterfallArtifactManifest

def create_manifest(manifest_id: str, items: list) -> WaterfallArtifactManifest:
    return WaterfallArtifactManifest(manifest_id=manifest_id, items=items)
