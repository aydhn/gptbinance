from typing import List, Dict


class ClusterRegistry:
    def __init__(self):
        self._clusters: Dict[str, List[str]] = {}

    def register_cluster(self, cluster_id: str, symbols: List[str]):
        self._clusters[cluster_id] = symbols

    def get_cluster(self, cluster_id: str) -> List[str]:
        return self._clusters.get(cluster_id, [])

    def evaluate_cluster_saturation(
        self, cluster_id: str, exposures: Dict[str, float]
    ) -> float:
        symbols = self.get_cluster(cluster_id)
        if not symbols:
            return 0.0
        return sum(exposures.get(sym, 0.0) for sym in symbols)


global_cluster_registry = ClusterRegistry()
