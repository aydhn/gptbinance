from app.governance.data_refresh import DataRefreshOrchestrator


def test_data_refresh():
    orch = DataRefreshOrchestrator()
    res = orch.refresh(None)
    assert res["status"] == "success"
    assert len(res["refreshed_datasets"]) > 0
