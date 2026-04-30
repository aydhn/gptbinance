from app.governance.ml_refresh import MLRefreshOrchestrator


def test_ml_refresh():
    orch = MLRefreshOrchestrator()
    res = orch.refresh(None)
    assert res["status"] == "success"
