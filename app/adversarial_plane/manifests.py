from typing import List, Dict, Any
from app.adversarial_plane.models import AdversarialArtifactManifest
import hashlib
import json

class ManifestBuilder:
    @staticmethod
    def build_manifest(manifest_id: str, data: Dict[str, Any]) -> AdversarialArtifactManifest:
        content_str = json.dumps(data, sort_keys=True)
        content_hash = hashlib.sha256(content_str.encode('utf-8')).hexdigest()

        return AdversarialArtifactManifest(
            manifest_id=manifest_id,
            actors_refs=data.get("actors", []),
            incentives_refs=data.get("incentives", []),
            surfaces_refs=data.get("surfaces", []),
            exploits_refs=data.get("exploits", []),
            controls_refs=data.get("controls", []),
            hash=content_hash
        )
