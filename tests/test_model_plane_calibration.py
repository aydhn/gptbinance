import pytest
from datetime import datetime, timezone, timedelta
from app.model_plane.calibration import CalibrationManager
from app.model_plane.models import CalibrationRecord
from app.model_plane.enums import CalibrationClass
from app.model_plane.exceptions import CalibrationError


def test_calibration_manager():
    manager = CalibrationManager(stale_threshold_days=7)

    fresh_date = datetime.now(timezone.utc) - timedelta(days=2)
    fresh_record = CalibrationRecord(
        record_id="cal_1",
        checkpoint_id="chk_1",
        evaluated_at=fresh_date,
        calibration_class=CalibrationClass.WELL_CALIBRATED,
        summary={"brier_score": 0.05},
    )
    manager.store_record(fresh_record)

    retrieved = manager.evaluate_calibration("chk_1")
    assert retrieved == fresh_record
    assert manager.check_calibration_freshness(retrieved) is False


def test_calibration_staleness():
    manager = CalibrationManager(stale_threshold_days=7)

    stale_date = datetime.now(timezone.utc) - timedelta(days=10)
    stale_record = CalibrationRecord(
        record_id="cal_2",
        checkpoint_id="chk_2",
        evaluated_at=stale_date,
        calibration_class=CalibrationClass.WELL_CALIBRATED,
        summary={},
    )
    manager.store_record(stale_record)

    assert manager.check_calibration_freshness(stale_record) is True


def test_calibration_missing():
    manager = CalibrationManager()
    with pytest.raises(CalibrationError):
        manager.evaluate_calibration("chk_missing")
