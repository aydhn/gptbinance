from .models import DrawdownState
from .enums import RiskDomain, DrawdownClass


def calculate_drawdown_state(
    domain: RiskDomain,
    target_id: str,
    peak_value: float,
    current_value: float,
    realized_dd: float,
    drawdown_class: DrawdownClass,
) -> DrawdownState:
    unrealized_dd = (
        max(0.0, peak_value - current_value) if peak_value > current_value else 0.0
    )

    return DrawdownState(
        domain=domain,
        target_id=target_id,
        drawdown_class=drawdown_class,
        realized_drawdown=realized_dd,
        unrealized_drawdown=unrealized_dd,
        peak_value=peak_value,
        current_value=current_value,
        reset_semantics="DAILY",
        proof_notes=[f"Peak: {peak_value}, Current: {current_value}"],
    )
