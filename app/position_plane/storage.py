
from typing import Any


class PositionStorage:
    """Mock storage layer representing SQLite/Parquet integration"""

    def __init__(self):
        self._lots = {}
        self._states = {}
        self._manifests = {}
        self._pnl_records = {}

    def save_state(self, state: Any):
        self._states[state.id] = state

    def get_state(self, state_id: str) -> Any:
        return self._states.get(state_id)

    def save_manifest(self, manifest: Any):
        self._manifests[manifest.manifest_id] = manifest
