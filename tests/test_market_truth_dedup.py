from app.market_truth.dedup import DuplicateDetector
from app.market_truth.enums import DedupVerdict


def test_dedup() -> None:
    detector = DuplicateDetector()
    assert detector.check_event("evt1").verdict == DedupVerdict.UNIQUE
    assert detector.check_event("evt1").verdict == DedupVerdict.DUPLICATE
