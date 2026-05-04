from app.capital.ladder import get_ladder, is_transition_allowed, get_next_logical_tier


def test_ladder_transitions():
    assert is_transition_allowed("paper_zero", "testnet_zero") is True
    assert is_transition_allowed("paper_zero", "live_caution_tier_1") is False

    assert get_next_logical_tier("canary_micro") == "canary_small"
