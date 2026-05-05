import pytest
from app.activation.history import HistoryTracker
from app.activation.repository import ActivationRepository


def test_history_tracker():
    repo = ActivationRepository()
    tracker = HistoryTracker(repo)
    tracker.record_event(
        "intent-1", "STAGE_TRANSITION", {"from": "PREFLIGHT", "to": "OBSERVE"}
    )

    history = repo.get_history("intent-1")
    assert len(history) > 0
    assert history[-1].event_type == "STAGE_TRANSITION"
