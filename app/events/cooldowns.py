from app.events.models import EventCooldownPolicy
from app.events.enums import CooldownMode

DEFAULT_POLICY = EventCooldownPolicy(
    policy_id="default",
    mode=CooldownMode.REDUCE_ONLY,
    pre_event_minutes=30,
    post_event_minutes=30,
)

STRICT_POLICY = EventCooldownPolicy(
    policy_id="strict",
    mode=CooldownMode.FULL_HALT,
    pre_event_minutes=60,
    post_event_minutes=60,
)


def get_policy_for_profile(profile_id: str) -> EventCooldownPolicy:
    if profile_id == "canary_live_caution":
        return STRICT_POLICY
    return DEFAULT_POLICY
