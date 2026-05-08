from typing import Dict, Any, Optional


class PerformanceStorage:
    def __init__(self):
        self._manifests = {}
        self._returns = {}
        self._attributions = {}
        self._trusts = {}

    def save_manifest(self, manifest_id: str, data: Dict[str, Any]):
        self._manifests[manifest_id] = data

    def get_manifest(self, manifest_id: str) -> Optional[Dict[str, Any]]:
        return self._manifests.get(manifest_id)

    def save_return(self, surface_id: str, data: Dict[str, Any]):
        self._returns[surface_id] = data

    def get_return(self, surface_id: str) -> Optional[Dict[str, Any]]:
        return self._returns.get(surface_id)

    def save_attribution(self, tree_id: str, data: Dict[str, Any]):
        self._attributions[tree_id] = data

    def save_trust(self, verdict_id: str, data: Dict[str, Any]):
        self._trusts[verdict_id] = data


global_performance_storage = PerformanceStorage()
