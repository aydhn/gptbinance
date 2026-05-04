from app.capital.performance import summarize_capital_performance


def test_summarize_capital_performance():
    metrics_ok = {
        "execution_count": 100,
        "realized_slippage_bps": 5.0,
        "order_reject_rate": 0.01,
        "max_drawdown_pct": 0.05,
    }
    res_ok = summarize_capital_performance(metrics_ok)
    assert res_ok["is_acceptable"] is True

    metrics_bad = {"execution_count": 10, "realized_slippage_bps": 20.0}
    res_bad = summarize_capital_performance(metrics_bad)
    assert res_bad["is_acceptable"] is False
    assert len(res_bad["warnings"]) == 2
