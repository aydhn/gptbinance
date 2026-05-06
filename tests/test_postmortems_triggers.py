from app.postmortems.triggers import TriggerDetector


def test_trigger_detector():
    detector = TriggerDetector()
    assert len(detector.detect({}, {})) == 0
