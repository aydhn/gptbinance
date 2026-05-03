from app.perf.latency import LatencyTracker


def test_latency_tracker():
    tracker = LatencyTracker()
    tracker.record("comp1", 10.0)
    tracker.record("comp1", 20.0)
    tracker.record("comp1", 30.0)
    summaries = tracker.get_summaries()
    assert len(summaries) == 1
    assert summaries[0].call_count == 3
    assert summaries[0].p50_ms == 20.0
