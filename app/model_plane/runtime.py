from typing import Dict, Optional, Any
from pydantic import BaseModel
from datetime import datetime, timezone
from app.model_plane.models import InferenceManifest, ModelPlaneBaseModel


class RuntimeInferenceSnapshot(ModelPlaneBaseModel):
    snapshot_id: str
    active_manifest_id: str
    timestamp: datetime
    session_id: str
    environment: str
    metadata: Dict[str, Any]
    active_release_bundle_ref: Optional[str] = None


class RuntimeModelContext:
    def __init__(self, active_release_bundle_ref: str = None):
        self._active_manifest: Optional[InferenceManifest] = None
        self._snapshots: Dict[str, RuntimeInferenceSnapshot] = {}
        self.active_release_bundle_ref = active_release_bundle_ref

    def set_active_manifest(self, manifest: InferenceManifest) -> None:
        self._active_manifest = manifest

    def get_active_manifest(self) -> Optional[InferenceManifest]:
        return self._active_manifest

    def create_snapshot(
        self, snapshot_id: str, session_id: str, environment: str = "live"
    ) -> RuntimeInferenceSnapshot:
        if not self._active_manifest:
            raise ValueError("No active manifest to snapshot")

        snapshot = RuntimeInferenceSnapshot(
            snapshot_id=snapshot_id,
            active_manifest_id=self._active_manifest.manifest_id,
            timestamp=datetime.now(timezone.utc),
            session_id=session_id,
            environment=environment,
            metadata={},
            active_release_bundle_ref=self.active_release_bundle_ref
        )
        self._snapshots[snapshot_id] = snapshot
        return snapshot

    def detect_silent_model_swap(self):
        # Silent model swap triggers release-plane hotfix divergence
        pass
