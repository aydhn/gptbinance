import pytest
from app.execution.live_runtime.rollout_modes import (
    get_default_caps_for_mode,
    is_real_order_submit_allowed,
)
from app.execution.live_runtime.enums import LiveRolloutMode


def test_rollout_modes_caps():
    shadow_caps = get_default_caps_for_mode(LiveRolloutMode.SHADOW_ONLY)
    assert shadow_caps.max_session_notional_usd == 0.0

    canary_caps = get_default_caps_for_mode(LiveRolloutMode.CANARY_LIVE)
    assert canary_caps.max_session_notional_usd > 0
    assert canary_caps.max_daily_loss_usd > 0

    locked_caps = get_default_caps_for_mode(LiveRolloutMode.FULL_LIVE_LOCKED)
    assert locked_caps.max_session_notional_usd == 0.0


def test_rollout_modes_real_orders():
    assert not is_real_order_submit_allowed(LiveRolloutMode.SHADOW_ONLY)
    assert not is_real_order_submit_allowed(LiveRolloutMode.TESTNET_EXEC)
    assert not is_real_order_submit_allowed(LiveRolloutMode.FULL_LIVE_LOCKED)
    assert is_real_order_submit_allowed(LiveRolloutMode.CANARY_LIVE)
    assert is_real_order_submit_allowed(LiveRolloutMode.CAPPED_LIVE)
