from decimal import Decimal
from typing import Tuple, Optional
from app.data_plane.snapshots import SnapshotManager


class MarkSourceEngine:
    @staticmethod
    def get_trusted_mark(
        symbol: str,
        current_time: float,
        last_update_time: float,
        price: Decimal,
        snapshot_manager: Optional[SnapshotManager] = None,
        snapshot_id: Optional[str] = None,
    ) -> Tuple[Decimal, float, str]:
        staleness = current_time - last_update_time
        confidence = 1.0

        if staleness > 60:
            confidence = max(0.0, 1.0 - (staleness - 60) / 300)

        source = "binance_ticker"

        if snapshot_manager and snapshot_id:
            snapshot = snapshot_manager.get(snapshot_id)
            if snapshot and "mark_price" in snapshot.data:
                price = Decimal(str(snapshot.data["mark_price"]))
                source = "canonical_snapshot"

        return price, confidence, source
