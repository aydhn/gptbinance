import pytest
from app.drift_plane.objects import DriftObjectManager
from app.drift_plane.enums import DriftClass
from app.drift_plane.exceptions import InvalidDriftObjectError

def test_drift_object_creation():
    manager = DriftObjectManager()
    obj = manager.create_object(
        drift_id="drift-obj-1",
        class_type=DriftClass.POST_NORMALIZATION_DRIFT,
        owner="owner-1",
        scope="scope-1",
        baseline_posture="stable",
        recurrence_posture="none"
    )

    assert obj.drift_id == "drift-obj-1"
    assert obj.class_type == DriftClass.POST_NORMALIZATION_DRIFT

def test_drift_object_creation_vague_name():
    manager = DriftObjectManager()
    with pytest.raises(InvalidDriftObjectError):
        manager.create_object(
            drift_id="",
            class_type=DriftClass.POST_NORMALIZATION_DRIFT,
            owner="owner-1",
            scope="scope-1",
            baseline_posture="stable",
            recurrence_posture="none"
        )
