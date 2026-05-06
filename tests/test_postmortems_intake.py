from app.postmortems.intake import IntakeManager


def test_intake_normalization():
    manager = IntakeManager()
    raw = {"data": "test"}
    normalized = manager.process_intake("incident", raw)
    assert normalized == raw
