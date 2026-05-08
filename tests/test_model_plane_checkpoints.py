import pytest
from datetime import datetime, timezone, timedelta
from app.model_plane.checkpoints import ModelCheckpointRegistry
from app.model_plane.models import ModelCheckpointRecord, ModelArtifactManifest
from app.model_plane.exceptions import InvalidCheckpointRecordError


def test_checkpoint_registry_valid():
    registry = ModelCheckpointRegistry()
    record = ModelCheckpointRecord(
        checkpoint_id="chk_1",
        model_id="model_1",
        created_at=datetime.now(timezone.utc),
        source_training_run_id="run_1",
        feature_manifest_id="feat_1",
        config_ref="conf_1",
        artifact=ModelArtifactManifest(
            artifact_id="art_1", checksum="abc", path="path/to/model"
        ),
    )
    registry.register_checkpoint(record)
    assert registry.get_checkpoint("chk_1") == record
    assert len(registry.get_checkpoints_for_model("model_1")) == 1


def test_checkpoint_registry_invalid():
    registry = ModelCheckpointRegistry()
    with pytest.raises(InvalidCheckpointRecordError):
        registry.register_checkpoint(
            ModelCheckpointRecord(
                checkpoint_id="",
                model_id="model_1",
                created_at=datetime.now(timezone.utc),
                source_training_run_id="run_1",
                feature_manifest_id="feat_1",
                config_ref="conf_1",
                artifact=ModelArtifactManifest(
                    artifact_id="art_1", checksum="abc", path="path/to/model"
                ),
            )
        )


def test_checkpoint_freshness():
    registry = ModelCheckpointRegistry(stale_threshold_days=30)

    fresh_date = datetime.now(timezone.utc) - timedelta(days=10)
    fresh_record = ModelCheckpointRecord(
        checkpoint_id="chk_fresh",
        model_id="model_1",
        created_at=fresh_date,
        source_training_run_id="run_1",
        feature_manifest_id="feat_1",
        config_ref="conf_1",
        artifact=ModelArtifactManifest(
            artifact_id="art_1", checksum="abc", path="path"
        ),
    )
    registry.register_checkpoint(fresh_record)

    stale_date = datetime.now(timezone.utc) - timedelta(days=40)
    stale_record = ModelCheckpointRecord(
        checkpoint_id="chk_stale",
        model_id="model_1",
        created_at=stale_date,
        source_training_run_id="run_1",
        feature_manifest_id="feat_1",
        config_ref="conf_1",
        artifact=ModelArtifactManifest(
            artifact_id="art_1", checksum="abc", path="path"
        ),
    )
    registry.register_checkpoint(stale_record)

    assert not registry.evaluate_freshness("chk_fresh")
    assert registry.evaluate_freshness("chk_stale")
    assert stale_record.is_stale == True
