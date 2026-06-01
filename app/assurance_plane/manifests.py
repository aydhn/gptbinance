from app.assurance_plane.models import AssuranceArtifactManifest
import hashlib
import json

def generate_manifest(manifest_id: str, assurance_id: str, data: dict) -> AssuranceArtifactManifest:
    serialized = json.dumps(data, sort_keys=True).encode("utf-8")
    hash_val = hashlib.sha256(serialized).hexdigest()
    return AssuranceArtifactManifest(
        manifest_id=manifest_id,
        assurance_id=assurance_id,
        hash_refs={"primary": hash_val}
    )
