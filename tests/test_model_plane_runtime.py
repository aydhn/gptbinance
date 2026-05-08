import pytest
from app.model_plane.runtime import RuntimeModelContext, RuntimeInferenceSnapshot
from app.model_plane.models import InferenceManifest
from datetime import datetime


def test_runtime_context_active_manifest():
    context = RuntimeModelContext()
    manifest = InferenceManifest(
        manifest_id="mf_1", entries=[], created_at=datetime.now()
    )
    context.set_active_manifest(manifest)
    assert context.get_active_manifest() == manifest


def test_runtime_snapshot_creation():
    context = RuntimeModelContext()
    manifest = InferenceManifest(
        manifest_id="mf_1", entries=[], created_at=datetime.now()
    )
    context.set_active_manifest(manifest)

    snapshot = context.create_snapshot("snap1", "sess1", "live")
    assert snapshot.snapshot_id == "snap1"
    assert snapshot.active_manifest_id == "mf_1"
    assert snapshot.session_id == "sess1"
    assert snapshot.environment == "live"


def test_runtime_snapshot_no_manifest():
    context = RuntimeModelContext()
    with pytest.raises(ValueError):
        context.create_snapshot("snap1", "sess1", "live")
