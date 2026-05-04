from app.crossbook.conflicts import ConflictDetector

def test_conflict_detector():
    detector = ConflictDetector()
    assert detector.detect() == []
