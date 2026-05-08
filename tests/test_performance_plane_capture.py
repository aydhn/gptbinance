from app.performance_plane.capture import CaptureAnalyzer


def test_capture_ratio_correctness():
    record = CaptureAnalyzer.calculate_ratio(
        step_name="signal_to_allocation", initial_opportunity=100.0, captured_value=80.0
    )

    assert record.ratio == 0.8
    assert record.step_name == "signal_to_allocation"
