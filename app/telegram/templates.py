"""Templates for Telegram messages."""

from typing import Dict, Any


def render_session_started(run_id: str, config: Any) -> str:
    symbols = ", ".join(config.symbols)
    return (
        f"🚀 <b>Paper Session Started</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Symbols: {symbols}\n"
        f"Features: {config.feature_set}\n"
        f"Strategy: {config.strategy_set}"
    )


def render_session_stopped(run_id: str, reason: str, summary: Any) -> str:
    return (
        f"🛑 <b>Paper Session Stopped</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Reason: {reason}\n"
        f"Orders: {summary.total_orders}\n"
        f"Fills: {summary.total_fills}\n"
        f"Final Equity: {summary.final_equity:.2f}\n"
        f"Max Drawdown: {summary.max_drawdown_pct:.2%}"
    )


def render_risk_veto_storm(run_id: str, symbol: str, count: int) -> str:
    return (
        f"⚠️ <b>Risk Veto Storm</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Symbol: {symbol}\n"
        f"{count} intents vetoed recently."
    )


def render_kill_switch_active(run_id: str, reason: str) -> str:
    return (
        f"🚨 <b>KILL SWITCH TRIGGERED</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Reason: {reason}"
    )


def render_stream_degraded(run_id: str, symbol: str, lag_ms: float) -> str:
    return (
        f"📉 <b>Stream Degraded</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Symbol: {symbol}\n"
        f"Lag: {lag_ms:.0f}ms"
    )


def render_paper_fill_summary(
    run_id: str, symbol: str, side: str, qty: float, price: float, pnl: float
) -> str:
    return (
        f"📝 <b>Paper Fill</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"{side} {qty} {symbol} @ {price:.2f}\n"
        f"Realized PnL: {pnl:.2f}"
    )


def render_pnl_milestone(run_id: str, pnl: float, equity: float) -> str:
    return (
        f"💰 <b>PnL Milestone</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"PnL: {pnl:.2f}\n"
        f"Equity: {equity:.2f}"
    )


def render_drawdown_warning(run_id: str, drawdown: float) -> str:
    return (
        f"📉 <b>Drawdown Warning</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Current Drawdown: {drawdown:.2%}"
    )


def render_daily_summary(run_id: str, summary: Any) -> str:
    return render_session_stopped(run_id, "daily_summary", summary)


def render_live_start(run_id: str, config: Any) -> str:
    symbols = (
        ", ".join([a.symbol for a in config.capital_caps.allowlist])
        if config.capital_caps.allowlist
        else "None"
    )
    return (
        f"🚨 <b>LIVE Session Started</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Mode: {config.rollout_mode.value}\n"
        f"Allowed Symbols: {symbols}\n"
        f"Max Session Notional: ${config.capital_caps.max_session_notional_usd:.2f}\n"
        f"Max Daily Loss: ${config.capital_caps.max_daily_loss_usd:.2f}"
    )


def render_live_cap_hit(run_id: str, cap_type: str, reason: str) -> str:
    return (
        f"🛑 <b>CAPITAL CAP HIT</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Type: {cap_type}\n"
        f"Reason: {reason}"
    )


def render_live_flatten(run_id: str, success: bool, cancelled: int, closed: int) -> str:
    status = "SUCCESS" if success else "FAILED/PARTIAL"
    return (
        f"🧹 <b>Live Session Flatten</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Status: {status}\n"
        f"Orders Cancelled: {cancelled}\n"
        f"Positions Closed: {closed}"
    )


def render_live_rollback(run_id: str, severity: str, reason: str) -> str:
    return (
        f"⏪ <b>Live Session Rollback</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Severity: {severity}\n"
        f"Reason: {reason}\n"
        f"Mainnet Disarmed."
    )
