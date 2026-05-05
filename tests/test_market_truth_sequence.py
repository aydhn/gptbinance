from app.market_truth.sequence import SequenceIntegrityEngine


def test_sequence_integrity():
    engine = SequenceIntegrityEngine()
    events = [{"id": 1}, {"id": 2}, {"id": 4}]
    res = engine.check_integrity(events)
    assert res.is_monotonic is True

    events_bad = [{"id": 1}, {"id": 3}, {"id": 2}]
    res_bad = engine.check_integrity(events_bad)
    assert res_bad.is_monotonic is False
