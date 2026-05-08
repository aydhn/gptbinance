import pytest
from app.model_plane.freshness import ModelFreshnessEvaluator
from app.model_plane.checkpoints import ModelCheckpointRegistry
from app.model_plane.calibration import CalibrationManager
from app.model_plane.models import (
    ModelCheckpointRecord,
    ModelArtifactManifest,
    CalibrationRecord,
)
from app.model_plane.enums import CalibrationClass
from datetime import datetime, timezone, timedelta


def test_model_freshness():
    chk_reg = ModelCheckpointRegistry(stale_threshold_days=30)
    cal_mgr = CalibrationManager(stale_threshold_days=7)
    evaluator = ModelFreshnessEvaluator(chk_reg, cal_mgr)

    # Setup fresh checkpoint and fresh calibration
    fresh_date = datetime.now(timezone.utc) - timedelta(days=2)
    chk_record = ModelCheckpointRecord(
        checkpoint_id="chk1",
        model_id="m1",
        created_at=fresh_date,
        source_training_run_id="r1",
        feature_manifest_id="f1",
        config_ref="c1",
        artifact=ModelArtifactManifest(artifact_id="a1", checksum="abc", path="path"),
    )
    chk_reg.register_checkpoint(chk_record)

    cal_record = CalibrationRecord(
        record_id="cal1",
        checkpoint_id="chk1",
        evaluated_at=fresh_date,
        calibration_class=CalibrationClass.WELL_CALIBRATED,
        summary={},
    )
    cal_mgr.store_record(cal_record)

    results = evaluator.evaluate_all("chk1")
    assert results["checkpoint_stale"] is False
    assert results["calibration_stale"] is False


def test_model_freshness_stale_calibration():
    chk_reg = ModelCheckpointRegistry(stale_threshold_days=30)
    cal_mgr = CalibrationManager(stale_threshold_days=7)
    evaluator = ModelFreshnessEvaluator(chk_reg, cal_mgr)

    # Setup fresh checkpoint but stale calibration
    fresh_date = datetime.now(timezone.utc) - timedelta(days=2)
    chk_record = ModelCheckpointRecord(
        checkpoint_id="chk1",
        model_id="m1",
        created_at=fresh_date,
        source_training_run_id="r1",
        feature_manifest_id="f1",
        config_ref="c1",
        artifact=ModelArtifactManifest(artifact_id="a1", checksum="abc", path="path"),
    )
    chk_reg.register_checkpoint(chk_record)

    stale_date = datetime.now(timezone.utc) - timedelta(days=10)
    cal_record = CalibrationRecord(
        record_id="cal1",
        checkpoint_id="chk1",
        evaluated_at=stale_date,
        calibration_class=CalibrationClass.WELL_CALIBRATED,
        summary={},
    )
    cal_mgr.store_record(cal_record)

    results = evaluator.evaluate_all("chk1")
    assert results["checkpoint_stale"] is False
    assert results["calibration_stale"] is True


def test_model_freshness_missing_calibration():
    chk_reg = ModelCheckpointRegistry(stale_threshold_days=30)
    cal_mgr = CalibrationManager(stale_threshold_days=7)
    evaluator = ModelFreshnessEvaluator(chk_reg, cal_mgr)

    # Setup fresh checkpoint, no calibration
    fresh_date = datetime.now(timezone.utc) - timedelta(days=2)
    chk_record = ModelCheckpointRecord(
        checkpoint_id="chk1",
        model_id="m1",
        created_at=fresh_date,
        source_training_run_id="r1",
        feature_manifest_id="f1",
        config_ref="c1",
        artifact=ModelArtifactManifest(artifact_id="a1", checksum="abc", path="path"),
    )
    chk_reg.register_checkpoint(chk_record)

    results = evaluator.evaluate_all("chk1")
    assert results["checkpoint_stale"] is False
    assert results["calibration_stale"] is True
    assert "No calibration record found" in results["warnings"]
