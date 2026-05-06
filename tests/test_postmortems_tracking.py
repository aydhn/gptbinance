from app.postmortems.tracking import ActionTracker


def test_action_tracking():
    tracker = ActionTracker()
    record = tracker.track("ACT-001")
    assert record.status == "open"
