from app.shadow_state.local import local_truth_adapter


def test_local_truth_adapter():
    snap = local_truth_adapter.fetch_snapshot("test_prof", "test_ws")
    assert snap.metadata.source.value == "local_derived"
    assert snap.account_mode_belief.get("futures_position_mode") == "HEDGE"
