import pytest
from app.drift_plane.recurrence import RecurrenceManager
from app.drift_plane.enums import RecurrenceClass

def test_recurrence_trigger_creation():
    manager = RecurrenceManager()
    manager.add_trigger("trigger-1", RecurrenceClass.ACTIVE)

    trigger = manager.get_trigger("trigger-1")
    assert trigger is not None
    assert trigger.trigger_id == "trigger-1"
    assert trigger.class_type == RecurrenceClass.ACTIVE
