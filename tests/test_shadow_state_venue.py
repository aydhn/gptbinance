from app.shadow_state.venue import venue_truth_adapter


def test_venue_truth_adapter():
    snap = venue_truth_adapter.fetch_snapshot("test_prof", "test_ws")
    assert snap.metadata.source.value == "venue"
    assert snap.modes.futures_position_mode == "HEDGE"
