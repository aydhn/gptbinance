from app.execution_plane.markouts import MarkoutEvaluator


def test_markout():
    # Buy, filled 100, market now 105. Favorable.
    rep1 = MarkoutEvaluator.evaluate("s1", 100.0, "buy", 105.0, 60000)
    assert rep1.is_favorable is True
    assert rep1.markout_bps == 500.0

    # Sell, filled 100, market now 105. Unfavorable.
    rep2 = MarkoutEvaluator.evaluate("s2", 100.0, "sell", 105.0, 60000)
    assert rep2.is_favorable is False
    assert rep2.markout_bps == -500.0
