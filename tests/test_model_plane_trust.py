import pytest
from app.model_plane.trust import TrustedSignalVerdictEngine
from app.model_plane.freshness import ModelFreshnessEvaluator
from app.model_plane.uncertainty import UncertaintyManager
from app.model_plane.checkpoints import ModelCheckpointRegistry
from app.model_plane.calibration import CalibrationManager
from app.model_plane.models import (
    InferenceManifestEntry,
    ModelRef,
    ModelCheckpointRecord,
    ModelArtifactManifest,
    CalibrationRecord,
    UncertaintyRecord,
)
from app.model_plane.enums import (
    TrustedSignalVerdict,
    CalibrationClass,
    UncertaintyClass,
)
from datetime import datetime, timezone


def setup_managers():
    chk_reg = ModelCheckpointRegistry(stale_threshold_days=30)
    cal_mgr = CalibrationManager(stale_threshold_days=7)
    fresh_eval = ModelFreshnessEvaluator(chk_reg, cal_mgr)
    unc_mgr = UncertaintyManager()

    # Setup fresh items
    now = datetime.now(timezone.utc)
    chk = ModelCheckpointRecord(
        checkpoint_id="chk1",
        model_id="m1",
        created_at=now,
        source_training_run_id="run1",
        feature_manifest_id="f1",
        config_ref="c1",
        artifact=ModelArtifactManifest(artifact_id="a1", checksum="abc", path="path"),
    )
    chk_reg.register_checkpoint(chk)

    cal = CalibrationRecord(
        record_id="cal1",
        checkpoint_id="chk1",
        evaluated_at=now,
        calibration_class=CalibrationClass.WELL_CALIBRATED,
        summary={},
    )
    cal_mgr.store_record(cal)

    unc = UncertaintyRecord(
        record_id="unc1",
        checkpoint_id="chk1",
        evaluated_at=now,
        uncertainty_class=UncertaintyClass.HIGH_CONFIDENCE,
        summary={},
    )
    unc_mgr.store_record(unc)

    return fresh_eval, unc_mgr


def test_trusted_signal_verdict_trusted():
    fresh_eval, unc_mgr = setup_managers()
    engine = TrustedSignalVerdictEngine(fresh_eval, unc_mgr)

    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
    )
    verdict = engine.evaluate(entry, feature_trust_degraded=False)

    assert verdict.verdict == TrustedSignalVerdict.TRUSTED
    assert len(verdict.blocker_reasons) == 0


def test_trusted_signal_verdict_degraded_features():
    fresh_eval, unc_mgr = setup_managers()
    engine = TrustedSignalVerdictEngine(fresh_eval, unc_mgr)

    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
    )
    verdict = engine.evaluate(entry, feature_trust_degraded=True)

    assert verdict.verdict == TrustedSignalVerdict.DEGRADED
    assert "Feature input trust is degraded" in verdict.blocker_reasons


def test_trusted_signal_verdict_low_confidence():
    fresh_eval, unc_mgr = setup_managers()
    engine = TrustedSignalVerdictEngine(fresh_eval, unc_mgr)

    # Overwrite uncertainty to low confidence
    unc = UncertaintyRecord(
        record_id="unc2",
        checkpoint_id="chk1",
        evaluated_at=datetime.now(timezone.utc),
        uncertainty_class=UncertaintyClass.LOW_CONFIDENCE,
        summary={},
    )
    unc_mgr.store_record(unc)

    entry = InferenceManifestEntry(
        model_ref=ModelRef(model_id="m1", version="1"), checkpoint_id="chk1"
    )
    verdict = engine.evaluate(entry, feature_trust_degraded=False)

    assert verdict.verdict == TrustedSignalVerdict.BLOCKED
    assert "Failed low confidence gate" in verdict.blocker_reasons
