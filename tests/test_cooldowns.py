from datetime import datetime, timezone, timedelta
from app.strategies.cooldowns import CooldownManager
from app.strategies.enums import CooldownScope


def test_cooldown_manager():
    manager = CooldownManager()
    now = datetime.now(timezone.utc)

    manager.apply_cooldown(CooldownScope.SYMBOL, "BTC", 300, "test", now)

    is_cd, reason = manager.is_in_cooldown(
        CooldownScope.SYMBOL, "BTC", now + timedelta(seconds=100)
    )
    assert is_cd

    is_cd, reason = manager.is_in_cooldown(
        CooldownScope.SYMBOL, "BTC", now + timedelta(seconds=400)
    )
    assert not is_cd

    assert not manager.check_all_scopes("ETH", "strat", "LONG", now)[0]
