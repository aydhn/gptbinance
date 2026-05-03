

from app.events.calendar_provider import DefaultCalendarProvider


def test_calendar_provider():
    provider = DefaultCalendarProvider()
    snap = provider.get_snapshot()
    assert snap.events
    assert snap.timestamp
