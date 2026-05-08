import pytest
from datetime import datetime, timezone
from app.model_plane.uncertainty import UncertaintyManager
from app.model_plane.models import UncertaintyRecord
from app.model_plane.enums import UncertaintyClass


def test_uncertainty_manager_low_confidence():
    manager = UncertaintyManager()

    record = UncertaintyRecord(
        record_id="unc_1",
        checkpoint_id="chk_1",
        evaluated_at=datetime.now(timezone.utc),
        uncertainty_class=UncertaintyClass.LOW_CONFIDENCE,
        summary={},
    )
    manager.store_record(record)

    assert manager.check_low_confidence_gate("chk_1") is False


def test_uncertainty_manager_high_confidence():
    manager = UncertaintyManager()

    record = UncertaintyRecord(
        record_id="unc_2",
        checkpoint_id="chk_2",
        evaluated_at=datetime.now(timezone.utc),
        uncertainty_class=UncertaintyClass.HIGH_CONFIDENCE,
        summary={},
    )
    manager.store_record(record)

    assert manager.check_low_confidence_gate("chk_2") is True


def test_uncertainty_manager_missing():
    manager = UncertaintyManager()
    assert manager.check_low_confidence_gate("chk_missing") is False
