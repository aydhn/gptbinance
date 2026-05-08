import uuid
from datetime import datetime, timezone
from app.config_plane.models import RuntimeConfigSnapshot


def capture_runtime_snapshot(
    manifest_id: str, active_profile: str
) -> RuntimeConfigSnapshot:
    return RuntimeConfigSnapshot(
        snapshot_id=f"rt_snap_{uuid.uuid4().hex[:8]}",
        effective_manifest_id=manifest_id,
        active_profile=active_profile,
        snapshot_at=datetime.now(timezone.utc),
    )
