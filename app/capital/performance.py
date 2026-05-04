from typing import Dict, Any


def summarize_capital_performance(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates capital performance not for alpha optimization,
    but for deployment quality signals required for capital tier escalation.
    """
    slippage_burden = metrics.get("realized_slippage_bps", 0.0)
    reject_rate = metrics.get("order_reject_rate", 0.0)
    max_dd = metrics.get("max_drawdown_pct", 0.0)
    sample_size = metrics.get("execution_count", 0)

    warnings = []
    acceptable = True

    if sample_size < 50:
        warnings.append("Insufficient sample size for reliable performance evaluation.")
        acceptable = False

    if slippage_burden > 10.0:
        warnings.append(f"High slippage burden: {slippage_burden} bps.")
        acceptable = False

    if reject_rate > 0.05:
        warnings.append(f"High order reject rate: {reject_rate * 100}%.")
        acceptable = False

    if max_dd > 0.15:
        warnings.append(f"High drawdown: {max_dd * 100}%.")
        acceptable = False

    return {"is_acceptable": acceptable, "warnings": warnings, "metrics": metrics}
