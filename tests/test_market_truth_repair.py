from app.market_truth.repair import SafeRepairPlanner


def test_repair():
    planner = SafeRepairPlanner()
    assert (
        planner.suggest_repair("SNAPSHOT_MISMATCH_GAP")
        == "refresh_market_truth_snapshot"
    )
