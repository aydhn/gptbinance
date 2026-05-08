from app.execution_plane.slippage import SlippageEvaluator
from app.execution_plane.enums import SlippageSeverityClass


def test_slippage_eval():
    # Buy, expected 100, filled 101. Diff = -1. Slippage = +1%. Bps = +100
    rep1 = SlippageEvaluator.evaluate("s1", 100.0, 101.0, "buy")
    assert rep1.realized_slippage_bps == 100.0
    assert rep1.severity == SlippageSeverityClass.CRITICAL

    # Sell, expected 100, filled 99. Diff = +1. Slippage = +1%. Bps = +100
    rep2 = SlippageEvaluator.evaluate("s2", 100.0, 99.0, "sell")
    assert rep2.realized_slippage_bps == 100.0
    assert rep2.severity == SlippageSeverityClass.CRITICAL

    # Good fill
    rep3 = SlippageEvaluator.evaluate("s3", 100.0, 100.0, "buy")
    assert rep3.realized_slippage_bps == 0.0
    assert rep3.severity == SlippageSeverityClass.NONE
