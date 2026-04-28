import logging
from typing import List
from app.backtest.walkforward.models import (
    WalkForwardConfig,
    WalkForwardPlan,
    WalkForwardWindow,
)
from app.backtest.walkforward.enums import WindowScheme
from app.backtest.walkforward.exceptions import InvalidWindowPlanError

logger = logging.getLogger(__name__)


# Assuming standard kline times. For simplicity, we assume we know the interval duration in ms.
# In a real app we'd resolve `interval` to ms.
def _interval_to_ms(interval: str) -> int:
    unit = interval[-1]
    val = int(interval[:-1])
    if unit == "m":
        return val * 60 * 1000
    elif unit == "h":
        return val * 60 * 60 * 1000
    elif unit == "d":
        return val * 24 * 60 * 60 * 1000
    else:
        # Default fallback, treat as 1m
        return 60 * 1000


class WindowGenerator:
    def generate(self, config: WalkForwardConfig) -> WalkForwardPlan:
        interval_ms = _interval_to_ms(config.interval)

        is_duration_ms = config.is_bars * interval_ms
        oos_duration_ms = config.oos_bars * interval_ms
        step_duration_ms = config.step_bars * interval_ms

        total_duration_ms = config.end_ts - config.start_ts

        if total_duration_ms < is_duration_ms + oos_duration_ms:
            logger.warning("Total duration is less than one complete IS + OOS window.")
            # We still generate a plan, it might just have 1 invalid window or 0 windows

        windows: List[WalkForwardWindow] = []

        current_is_start = config.start_ts
        current_is_end = current_is_start + is_duration_ms
        current_oos_start = current_is_end
        current_oos_end = current_oos_start + oos_duration_ms

        segment_index = 1

        while current_is_end < config.end_ts:
            # Check if OOS goes out of bounds, adjust if needed
            is_valid = True
            reason = None
            actual_oos_end = current_oos_end
            actual_oos_length = config.oos_bars

            if current_oos_end > config.end_ts:
                actual_oos_end = config.end_ts
                actual_oos_length = int(
                    (actual_oos_end - current_oos_start) / interval_ms
                )
                if (
                    actual_oos_length < config.min_trades_oos
                ):  # Just a heuristic, if very short
                    is_valid = False
                    reason = (
                        f"OOS period truncated to {actual_oos_length} bars, too short."
                    )
                else:
                    reason = f"OOS period truncated to {actual_oos_length} bars at the end of dataset."

            windows.append(
                WalkForwardWindow(
                    segment_index=segment_index,
                    is_start=current_is_start,
                    is_end=current_is_end,
                    oos_start=current_oos_start,
                    oos_end=actual_oos_end,
                    is_length=int((current_is_end - current_is_start) / interval_ms),
                    oos_length=actual_oos_length,
                    is_valid=is_valid,
                    reason=reason,
                )
            )

            # Step forward based on scheme
            if config.window_scheme == WindowScheme.ROLLING:
                current_is_start += step_duration_ms
                current_is_end += step_duration_ms
            elif config.window_scheme == WindowScheme.ANCHORED:
                current_is_end += step_duration_ms
            elif config.window_scheme == WindowScheme.EXPANDING:
                # Expanding is similar to anchored but maybe OOS is also different?
                # According to standard definition: IS expands, OOS steps forward.
                current_is_end += step_duration_ms
                # In expanding, maybe step size applies differently. Let's stick to simple expanding: IS grows.

            current_oos_start = current_is_end
            current_oos_end = current_oos_start + oos_duration_ms
            segment_index += 1

            # Stop if we can't form another full IS window (or any IS window)
            if current_is_start >= config.end_ts:
                break

        if not windows:
            raise InvalidWindowPlanError(
                "Could not generate any windows with the given config and dataset length."
            )

        return WalkForwardPlan(config=config, windows=windows)
