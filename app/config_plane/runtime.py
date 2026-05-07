from app.config_plane.models import RuntimeConfigSnapshot
from datetime import datetime, timezone


class RuntimeConfigManager:
    def take_snapshot(
        self, manifest_ref: str, config_hash: str
    ) -> RuntimeConfigSnapshot:
        return RuntimeConfigSnapshot(
            snapshot_id="rt_snap_" + str(int(datetime.now().timestamp())),
            captured_at=datetime.now(timezone.utc),
            active_manifest_ref=manifest_ref,
            active_hash=config_hash,
        )
