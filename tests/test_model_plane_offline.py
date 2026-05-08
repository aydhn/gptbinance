import pytest
from app.model_plane.offline import OfflineEvaluationEngine
from app.model_plane.inference import InferenceDescriptorLayer
from app.model_plane.models import InferenceManifest, InferenceManifestEntry, ModelRef
from datetime import datetime


def test_offline_scoring_empty_manifest():
    layer = InferenceDescriptorLayer()
    engine = OfflineEvaluationEngine(layer)

    manifest = InferenceManifest(
        manifest_id="mf_1", entries=[], created_at=datetime.now()
    )

    run = engine.run_deterministic_scoring("run_1", manifest, "ds_1", [{"feature1": 1}])
    assert run.scored_records == 1
    assert "No models in manifest" in run.caveats[0]


def test_offline_scoring_valid_manifest():
    layer = InferenceDescriptorLayer()
    engine = OfflineEvaluationEngine(layer)

    manifest = InferenceManifest(
        manifest_id="mf_1",
        entries=[
            InferenceManifestEntry(
                model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
            )
        ],
        created_at=datetime.now(),
    )

    inputs = [{"f1": 1}, {"f1": 2}, {"f1": 3}]
    run = engine.run_deterministic_scoring("run_1", manifest, "ds_1", inputs)

    assert run.scored_records == 3
    assert len(run.caveats) == 0
