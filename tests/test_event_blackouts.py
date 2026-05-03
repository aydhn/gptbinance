
from datetime import datetime, timezone, timedelta
from app.events.blackouts import BlackoutManager


def test_blackout_manager():
    manager = BlackoutManager()
    now = datetime.now(timezone.utc)
    manager.add_manual_blackout(
        now - timedelta(hours=1), now + timedelta(hours=1), "Testing"
    )
    active = manager.get_active_blackouts(now)
    assert len(active) == 1
    assert active[0].reason == "Testing"
