from app.data_plane.gaps import GapDetector


def test_gap_detector():
    detector = GapDetector()
    # 1000ms intervals. Gap between 2000 and 4000
    timestamps = [1000.0, 2000.0, 4000.0, 5000.0]
    gaps = detector.detect_missing_bars(timestamps, 1000)

    assert len(gaps) == 1
    assert gaps[0].gap_id == "gap_2000.0_4000.0"
