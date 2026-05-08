# Updated with Data Plane Integration
from app.data_plane.snapshots import SnapshotManager
from app.data_plane.trust import TrustEngine


class MarketTruthEvaluator:
    def evaluate_truth(
        self,
        snapshot_id: str,
        snapshot_manager: SnapshotManager,
        trust_engine: TrustEngine,
    ):
        snapshot = snapshot_manager.get(snapshot_id)
        if not snapshot:
            return None
        trust_verdict = trust_engine.evaluate({"snapshot_id": snapshot_id})
        return {"snapshot": snapshot, "trust_verdict": trust_verdict}
