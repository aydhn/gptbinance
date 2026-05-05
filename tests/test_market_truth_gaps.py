from app.market_truth.gaps import GapDetector
from app.market_truth.enums import GapType


def test_gap_detection():
    detector = GapDetector()
    ids = [1, 2, 4, 10]
    res = detector.detect_gaps(ids)
    assert len(res.findings) == 2
    assert res.findings[0].gap_type == GapType.TRANSIENT_GAP
    assert res.findings[1].gap_type == GapType.PERSISTENT_GAP
