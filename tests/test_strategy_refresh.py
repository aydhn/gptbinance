from app.governance.strategy_refresh import StrategyRefreshOrchestrator


def test_strategy_refresh():
    orch = StrategyRefreshOrchestrator()
    res = orch.refresh(None, {})
    assert res["status"] == "success"
