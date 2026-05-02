"""Templates for Telegram messages."""

from typing import Any


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


def render_portfolio_summary(run_id: str, summary: Any) -> str:
    return (
        f"📊 <b>Portfolio Allocation Summary</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Evaluated: {summary.total_intents_evaluated}\n"
        f"Approved: {summary.total_approved}\n"
        f"Reduced: {summary.total_reduced}\n"
        f"Deferred: {summary.total_deferred}\n"
        f"Rejected: {summary.total_rejected}\n"
        f"Allocated Notional: ${summary.total_allocated_notional:.2f}\n"
        f"Concentration: {summary.concentration_severity.value}"
    )


def render_concentration_warning(run_id: str, severity: str, breaches: list) -> str:
    breach_str = "\n".join([f"  - {b}" for b in breaches])
    return (
        f"⚠️ <b>Portfolio Concentration Warning</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Severity: {severity}\n"
        f"Breaches:\n{breach_str}"
    )


def render_capital_exhausted(run_id: str, available: float) -> str:
    return (
        f"💸 <b>Capital Budget Exhausted</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Remaining Available: ${available:.2f}\n"
        f"New allocations may be deferred or rejected."
    )


def render_cluster_crowding(run_id: str, cluster_id: str) -> str:
    return (
        f"🐑 <b>Correlated Cluster Crowding</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Cluster: {cluster_id}\n"
        f"Allocations into this cluster are being penalized."
    )


ML_TRAINING_COMPLETED = "🤖 ML Training Completed\nRun ID: {run_id}\nF1: {f1}"
ML_PROMOTION_RESULT = (
    "🤖 ML Promotion Check\nRun ID: {run_id}\nVerdict: {verdict}\nReasons: {reasons}"
)
ML_DRIFT_WARNING = (
    "⚠️ ML Drift Warning\nRun ID: {run_id}\nSeverity: {severity}\nAction: {action}"
)

GOVERNANCE_REFRESH_COMPLETED = "Governance refresh {run_id} completed. Status: {status}"
GOVERNANCE_DECAY_WARNING = (
    "Decay warning for {bundle_id}. Type: {degradation_type}, Severity: {severity}"
)
GOVERNANCE_PROMOTION_BLOCKED = "Promotion for {bundle_id} blocked. Blockers: {blockers}"

# Phase 22 Analytics Templates


def render_execution_quality_degraded(run_id: str, submit: int, rej: int) -> str:
    return (
        f"🚨 <b>Execution Quality Degraded</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Submit: {submit}, Rejects: {rej}"
    )


def render_divergence_warning(
    run_id: str, div_type: str, severity: str, evidence: str
) -> str:
    return (
        f"⚠️ <b>Divergence Warning</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Type: {div_type}\n"
        f"Severity: {severity}\n"
        f"Evidence: {evidence}"
    )


def render_anomaly_cluster(run_id: str, anomaly_type: str, evidence: str) -> str:
    return (
        f"👽 <b>Anomaly Cluster Detected</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Type: {anomaly_type}\n"
        f"Evidence: {evidence}"
    )


def render_strategy_decay_warning(run_id: str, family: str, hit_rate: float) -> str:
    return (
        f"📉 <b>Strategy Decay Warning</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Family: {family}\n"
        f"Hit Rate dropped to: {hit_rate*100:.1f}%"
    )


def render_root_cause_summary(run_id: str, hypothesis_id: str, causes: list) -> str:
    c_str = "\n".join([f" - {c}" for c in causes])
    return (
        f"🔬 <b>Root Cause Hypothesis</b>\n"
        f"Run ID: <code>{run_id}</code>\n"
        f"Hypothesis ID: {hypothesis_id}\n"
        f"Probable Causes:\n{c_str}"
    )


def format_job_failed_message(job_name: str, job_id: str, error: str) -> str:
    return f"🚨 *AUTOMATION JOB FAILED*\n\nJob: `{job_name}` (`{job_id}`)\nError: `{error}`\nStatus: Manual intervention may be required."


def format_retry_exhausted_message(job_name: str, attempts: int) -> str:
    return f"⚠️ *RETRY EXHAUSTED*\n\nJob: `{job_name}`\nFailed after `{attempts}` attempts."


def format_workflow_blocked_message(workflow_name: str, reason: str) -> str:
    return f"🛑 *WORKFLOW BLOCKED*\n\nWorkflow: `{workflow_name}`\nReason: `{reason}`"


def format_nightly_refresh_completed() -> str:
    return "✅ *NIGHTLY REFRESH COMPLETED*\n\nData and feature environments are updated."


def format_daily_analytics_ready() -> str:
    return "📊 *DAILY ANALYTICS READY*\n\nDaily analytics and reconciliations are available."


def format_maintenance_defer_notice(job_name: str) -> str:
    return f"⏸️ *JOB DEFERRED*\n\nJob: `{job_name}`\nDeferred due to active maintenance window."


def format_readiness_failed_scheduled_run(job_name: str) -> str:
    return f"❌ *READINESS CHECK FAILED*\n\nScheduled check `{job_name}` failed."


def render_release_built(version: str) -> str:
    return f"📦 <b>RELEASE BUILT: {version}</b>\nBundle is ready for verification."


def render_host_probe_failed(version: str, errors: list) -> str:
    err_str = "\n- ".join(errors)
    return f"❌ <b>HOST PROBE FAILED: {version}</b>\nErrors:\n- {err_str}"


def render_upgrade_blocked(version: str, reason: str) -> str:
    return f"🚫 <b>UPGRADE BLOCKED: {version}</b>\nReason: {reason}"


def render_health_degraded(component: str, severity: str, explanation: str) -> str:
    return f"⚠️ <b>HEALTH DEGRADED</b>\nComponent: {component}\nSeverity: {severity}\nReason: {explanation}"


def render_critical_alert(
    alert_id: str, component: str, rule: str, evidence: dict
) -> str:
    return f"🚨 <b>CRITICAL ALERT</b>\nID: {alert_id}\nComponent: {component}\nRule: {rule}\nEvidence: {evidence}"


def render_correlated_incident(
    group_id: str, primary_alert: str, likely_issue: str
) -> str:
    return f"🔗 <b>INCIDENT CORRELATION</b>\nGroup: {group_id}\nPrimary Alert: {primary_alert}\nLikely Issue: {likely_issue}"


def render_slo_breach(slo_id: str, current: float, explanation: str) -> str:
    return f"📉 <b>SLO BREACH</b>\nSLO ID: {slo_id}\nCurrent: {current}\nReason: {explanation}"


def render_observability_digest(scope: str, top_alerts: list, highlights: str) -> str:
    alerts_str = ", ".join(top_alerts) if top_alerts else "None"
    return f"📊 <b>OBSERVABILITY DIGEST ({scope})</b>\nTop Alerts: {alerts_str}\nHighlights: {highlights}"


def render_approval_requested(req_id: str, action: str, ttl: int) -> str:
    return f"📝 <b>Approval Requested</b>\nReq ID: {req_id}\nAction: {action}\nExpires in: {ttl}s"


def render_approval_expiring(req_id: str, action: str) -> str:
    return f"⏳ <b>Approval Expiring Soon</b>\nReq ID: {req_id}\nAction: {action}"


def render_critical_action_approved(req_id: str, action: str) -> str:
    return f"✅ <b>Critical Action Approved</b>\nReq ID: {req_id}\nAction: {action}"


def render_authorization_denied(req_id: str, reason: str) -> str:
    return f"🚫 <b>Authorization Denied</b>\nReq ID: {req_id}\nReason: {reason}"


def render_break_glass_triggered(
    req_id: str, operator_id: str, justification: str
) -> str:
    return f"🚨 <b>BREAK-GLASS TRIGGERED</b>\nReq ID: {req_id}\nOperator: {operator_id}\nJustification: {justification}\nImmediate review required."


def render_action_revoked(req_id: str, operator_id: str, reason: str) -> str:
    return f"❌ <b>Action Revoked</b>\nReq ID: {req_id}\nOperator: {operator_id}\nReason: {reason}"
