from typing import Dict
from app.execution.live_runtime.enums import LiveRolloutMode
from app.execution.live_runtime.models import LiveCapitalCaps


def get_default_caps_for_mode(mode: LiveRolloutMode) -> LiveCapitalCaps:
    if mode == LiveRolloutMode.SHADOW_ONLY:
        return LiveCapitalCaps(
            max_session_notional_usd=0.0,
            max_daily_loss_usd=0.0,
            max_live_exposure_usd=0.0,
            max_new_orders_per_session=0,
        )
    elif mode == LiveRolloutMode.TESTNET_EXEC:
        return LiveCapitalCaps(
            max_session_notional_usd=100000.0,
            max_daily_loss_usd=5000.0,
            max_live_exposure_usd=50000.0,
            max_new_orders_per_session=1000,
        )
    elif mode == LiveRolloutMode.CANARY_LIVE:
        return LiveCapitalCaps(
            max_session_notional_usd=100.0,
            max_daily_loss_usd=10.0,
            max_live_exposure_usd=50.0,
            max_new_orders_per_session=5,
        )
    elif mode == LiveRolloutMode.CAPPED_LIVE:
        return LiveCapitalCaps(
            max_session_notional_usd=1000.0,
            max_daily_loss_usd=100.0,
            max_live_exposure_usd=500.0,
            max_new_orders_per_session=50,
        )
    elif mode == LiveRolloutMode.FULL_LIVE_LOCKED:
        return LiveCapitalCaps(
            max_session_notional_usd=0.0,
            max_daily_loss_usd=0.0,
            max_live_exposure_usd=0.0,
            max_new_orders_per_session=0,
        )
    else:
        raise ValueError(f"Unknown mode: {mode}")


def is_real_order_submit_allowed(mode: LiveRolloutMode) -> bool:
    return mode in [LiveRolloutMode.CANARY_LIVE, LiveRolloutMode.CAPPED_LIVE]
