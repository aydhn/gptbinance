from app.events.cooldowns import get_policy_for_profile
from app.events.enums import CooldownMode


def test_get_policy():
    strict = get_policy_for_profile("canary_live_caution")
    assert strict.mode == CooldownMode.FULL_HALT

    default = get_policy_for_profile("default")
    assert default.mode == CooldownMode.REDUCE_ONLY
