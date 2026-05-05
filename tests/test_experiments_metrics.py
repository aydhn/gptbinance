from app.experiments.metrics import MetricsCollector


def test_metrics_collector():
    collector = MetricsCollector()
    metrics = collector.collect({"pnl_delta": 0.05, "trade_count_delta": 2})
    assert metrics["pnl"] == 0.05
    assert metrics["trade_count"] == 2
    assert metrics["friction"] == 0
