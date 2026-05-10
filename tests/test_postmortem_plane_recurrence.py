import pytest
from app.postmortem_plane.recurrence import RecurrenceTracker
from app.postmortem_plane.enums import RecurrenceClass, RecurrenceEscalationClass

def test_recurrence_tracker():
    r = RecurrenceTracker.track("R-1", RecurrenceClass.SAME_FAMILY, "FAM-A", 10, RecurrenceEscalationClass.ESCALATED, "Same timeout issue")
    assert r.recurrence_id == "R-1"
    assert r.escalation_class == RecurrenceEscalationClass.ESCALATED
