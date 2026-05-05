from app.events.sources import DummyMacroCalendarAdapter
from app.events.enums import EventFreshness


def test_dummy_macro_calendar():
    adapter = DummyMacroCalendarAdapter()
    events = adapter.fetch_events()
    assert len(events) > 0
    assert "US CPI Release" in events[0]["title"]

    health = adapter.get_source_health()
    assert health["status"] == "ok"
    assert health["freshness"] == EventFreshness.FRESH.value
