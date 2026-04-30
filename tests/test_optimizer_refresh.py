from app.governance.optimizer_refresh import OptimizerRefreshOrchestrator


def test_optimizer_refresh():
    orch = OptimizerRefreshOrchestrator()
    res = orch.refresh(None)
    assert res["status"] == "success"
