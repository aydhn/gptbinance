from datetime import datetime, timezone
from typing import List
from app.supply_chain.models import (
    BuildOutputManifest,
    BuildInputManifest,
    BuildArtifactRecord,
)
from app.supply_chain.enums import ArtifactClass
from app.supply_chain.hashes import generate_hash, stable_serialize


class ManifestBuilder:
    def build(
        self,
        inputs: BuildInputManifest,
        artifacts: List[BuildArtifactRecord],
        artifact_class: ArtifactClass,
    ) -> BuildOutputManifest:
        data = {
            "inputs": inputs.model_dump(),
            "artifacts": [a.model_dump() for a in artifacts],
            "class": artifact_class.value,
        }
        manifest_hash = generate_hash(stable_serialize(data))

        return BuildOutputManifest(
            id=f"man_{manifest_hash[:8]}",
            artifact_class=artifact_class,
            timestamp=datetime.now(timezone.utc),
            inputs=inputs,
            artifacts=artifacts,
            hash=manifest_hash,
        )
