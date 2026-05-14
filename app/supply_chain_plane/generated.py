from typing import Dict, List, Optional
from app.supply_chain_plane.models import GeneratedArtifactRecord


class GeneratedArtifactRegistry:
    def __init__(self):
        self._artifacts: Dict[str, GeneratedArtifactRecord] = {}

    def register_artifact(self, artifact: GeneratedArtifactRecord) -> None:
        self._artifacts[artifact.artifact_id] = artifact

    def get_artifact(self, artifact_id: str) -> Optional[GeneratedArtifactRecord]:
        return self._artifacts.get(artifact_id)
