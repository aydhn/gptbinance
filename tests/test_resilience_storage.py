from app.resilience.storage import StorageLayer
from app.resilience.models import ExperimentSummary, ExperimentGateReport
from app.resilience.enums import SafeScope, ExperimentStatus, GateVerdict
from datetime import datetime, timezone


def test_storage_layer():
    storage = StorageLayer()
    summary = ExperimentSummary(
        run_id="test_run",
        definition_id="test_def",
        scope=SafeScope.PAPER,
        status=ExperimentStatus.COMPLETED,
        start_time=datetime.now(timezone.utc),
        gate_report=ExperimentGateReport(verdict=GateVerdict.ALLOW, reason="ok"),
    )

    storage.save_summary(summary)
    retrieved = storage.get_summary("test_run")

    assert retrieved is not None
    assert retrieved.run_id == "test_run"
