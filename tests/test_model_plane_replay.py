import pytest
from app.model_plane.replay import ReplayContext
from app.model_plane.manifests import InferenceManifestBuilder
from app.model_plane.models import InferenceManifest, InferenceManifestEntry, ModelRef
from datetime import datetime


def test_replay_context_manifest_found():
    builder = InferenceManifestBuilder()
    manifest = InferenceManifest(
        manifest_id="mf_1",
        entries=[
            InferenceManifestEntry(
                model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
            )
        ],
        created_at=datetime.now(),
    )
    builder.store_manifest(manifest)

    ctx = ReplayContext(builder)
    recon = ctx.reconstruct_manifest("recon_1", datetime.now(), "mf_1")

    assert recon.reconstruction_id == "recon_1"
    assert recon.manifest_id == "mf_1"
    assert recon.confidence_score == 1.0
    assert len(recon.caveats) == 0


def test_replay_context_manifest_missing():
    builder = InferenceManifestBuilder()
    ctx = ReplayContext(builder)

    recon = ctx.reconstruct_manifest("recon_1", datetime.now(), "mf_missing")

    assert recon.manifest_id == "mf_missing"
    assert recon.confidence_score == 0.0
    assert "not found" in recon.caveats[0]
