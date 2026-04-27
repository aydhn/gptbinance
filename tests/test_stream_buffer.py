import pytest
from app.data.stream_buffer import StreamBuffer


class DummyEventA:
    def __init__(self, val: int):
        self.val = val


def test_stream_buffer_capacity():
    buffer = StreamBuffer(max_len_per_type=5)

    for i in range(10):
        buffer.add_event(DummyEventA(i))

    events = buffer.get_recent_events(DummyEventA, limit=10)
    assert len(events) == 5
    # The last 5 should be 5, 6, 7, 8, 9
    assert events[0].val == 5
    assert events[-1].val == 9


def test_stream_buffer_limit():
    buffer = StreamBuffer(max_len_per_type=10)

    for i in range(5):
        buffer.add_event(DummyEventA(i))

    events = buffer.get_recent_events(DummyEventA, limit=2)
    assert len(events) == 2
    assert events[0].val == 3
    assert events[1].val == 4


def test_stream_buffer_snapshot():
    buffer = StreamBuffer()
    buffer.add_event(DummyEventA(1))
    buffer.add_event(DummyEventA(2))

    snap = buffer.get_snapshot()
    assert "DummyEventA" in snap
    assert snap["DummyEventA"] == 2
