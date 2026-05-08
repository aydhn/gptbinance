from app.execution_plane.fills import FillQualityEvaluator
from app.execution_plane.enums import FillQualityClass


def test_fills():
    rep1 = FillQualityEvaluator.evaluate("s1", 100.0, 100.0, 50.0, is_maker=True)
    assert rep1.quality_class == FillQualityClass.PERFECT
    assert rep1.maker_taker_mix["maker"] == 1.0

    rep2 = FillQualityEvaluator.evaluate("s2", 5.0, 100.0, 50.0, is_maker=False)
    assert rep2.quality_class == FillQualityClass.POOR
    assert "extreme_partial_fill" in rep2.anomalies
