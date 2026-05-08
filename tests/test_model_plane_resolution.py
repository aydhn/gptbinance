import pytest
from app.model_plane.resolution import ModelResolutionEngine, ModelResolutionReport
from app.model_plane.models import InferenceManifest, InferenceManifestEntry, ModelRef
from datetime import datetime


def test_resolve_manifest_empty():
    engine = ModelResolutionEngine()
    manifest = InferenceManifest(
        manifest_id="mf_1", entries=[], created_at=datetime.now()
    )
    report = engine.resolve_manifest(manifest)
    assert "Manifest contains no entries" in report.blockers


def test_resolve_manifest_valid():
    engine = ModelResolutionEngine()
    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"),
        checkpoint_id="chk1",
        threshold_policy_id="tp1",
    )
    manifest = InferenceManifest(
        manifest_id="mf_1",
        entries=[entry],
        ensemble_policy_id="ens1",
        created_at=datetime.now(),
    )
    report = engine.resolve_manifest(manifest)

    assert "m1" in report.resolved_components
    assert report.resolved_components["m1"]["checkpoint_id"] == "chk1"
    assert len(report.blockers) == 0
    assert any("ens1" in note for note in report.proof_notes)


def test_resolve_manifest_missing_threshold():
    engine = ModelResolutionEngine()
    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"),
        checkpoint_id="chk1",
        threshold_policy_id=None,
    )
    manifest = InferenceManifest(
        manifest_id="mf_1", entries=[entry], created_at=datetime.now()
    )
    report = engine.resolve_manifest(manifest)

    assert "m1" in report.resolved_components
    assert any("No threshold policy specified" in note for note in report.proof_notes)
