from app.resilience.telemetry import ExperimentTelemetry


def test_experiment_telemetry():
    telemetry = ExperimentTelemetry()
    run_id = "test_run"

    telemetry.record_event(run_id, "test_event", {"key": "value"})

    timeline = telemetry.get_timeline(run_id)
    assert len(timeline) == 1
    assert timeline[0].event_type == "test_event"
    assert timeline[0].details == {"key": "value"}
