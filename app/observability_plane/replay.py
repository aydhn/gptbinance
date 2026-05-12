from typing import Dict, List, Optional
from .exceptions import ObservabilityPlaneError

class ReplayReconstructionTracker:
    def __init__(self):
        self._manifests: Dict[str, str] = {}

    def report_reconstruction(self, replay_id: str, manifest_id: str) -> None:
        self._manifests[replay_id] = manifest_id

    def get_reconstruction(self, replay_id: str) -> Optional[str]:
        return self._manifests.get(replay_id)

    def list_reconstructions(self) -> Dict[str, str]:
        return self._manifests.copy()
