import pytest
from datetime import datetime
from app.model_plane.manifests import InferenceManifestBuilder
from app.model_plane.models import InferenceManifest, InferenceManifestEntry, ModelRef
from app.model_plane.exceptions import ModelPlaneError


def test_manifest_builder_valid():
    builder = InferenceManifestBuilder()
    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"),
        checkpoint_id="chk1",
        threshold_policy_id="tp1",
    )
    manifest = InferenceManifest(
        manifest_id="manifest_1", entries=[entry], created_at=datetime.now()
    )
    builder.store_manifest(manifest)
    assert builder.get_manifest("manifest_1") == manifest
    assert len(builder.list_manifests()) == 1


def test_manifest_builder_missing_id():
    builder = InferenceManifestBuilder()
    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
    )
    with pytest.raises(ModelPlaneError):
        builder.store_manifest(
            InferenceManifest(
                manifest_id="", entries=[entry], created_at=datetime.now()
            )
        )


def test_manifest_builder_no_entries():
    builder = InferenceManifestBuilder()
    with pytest.raises(ModelPlaneError):
        builder.store_manifest(
            InferenceManifest(
                manifest_id="manifest_1", entries=[], created_at=datetime.now()
            )
        )
