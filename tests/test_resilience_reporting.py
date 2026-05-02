from app.resilience.reporting import Reporter
from app.resilience.models import ExperimentSummary, ExperimentGateReport
from app.resilience.enums import SafeScope, ExperimentStatus, GateVerdict
from datetime import datetime, timezone
import json


def test_reporter_generate_summary():
    summary = ExperimentSummary(
        run_id="test_run",
        definition_id="test_def",
        scope=SafeScope.PAPER,
        status=ExperimentStatus.COMPLETED,
        start_time=datetime.now(timezone.utc),
        gate_report=ExperimentGateReport(verdict=GateVerdict.ALLOW, reason="ok"),
    )

    report_json = Reporter.generate_summary(summary)
    report_dict = json.loads(report_json)

    assert report_dict["run_id"] == "test_run"
    assert report_dict["status"] == "completed"
