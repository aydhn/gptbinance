from datetime import datetime, timezone
import uuid
from app.shadow_state.models import LocalDerivedSnapshot, SnapshotMetadata
from app.shadow_state.enums import SnapshotSource, SnapshotFreshness


class LocalTruthAdapter:
    """Mock adapter for gathering local derived state."""

    def fetch_snapshot(
        self, profile_id: str, workspace_id: str
    ) -> LocalDerivedSnapshot:
        # Real impl would query order_lifecycle, ledger, crossbook, intent, capital
        metadata = SnapshotMetadata(
            snapshot_id=f"loc_{uuid.uuid4().hex[:8]}",
            source=SnapshotSource.LOCAL_DERIVED,
            timestamp=datetime.now(timezone.utc),
            profile_id=profile_id,
            workspace_id=workspace_id,
            freshness=SnapshotFreshness.FRESH,
        )

        return LocalDerivedSnapshot(
            metadata=metadata,
            active_attempts=[],
            ledger_balances=[],
            crossbook_posture={},
            risk_exposure={},
            account_mode_belief={
                "futures_position_mode": "HEDGE",
                "margin_mode": "CROSS",
            },
            capital_refs={},
            completeness_summary="Complete",
        )


local_truth_adapter = LocalTruthAdapter()
