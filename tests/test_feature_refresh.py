from app.governance.feature_refresh import FeatureRefreshOrchestrator


def test_feature_refresh():
    orch = FeatureRefreshOrchestrator()
    res = orch.refresh(None, {})
    assert res["status"] == "success"
