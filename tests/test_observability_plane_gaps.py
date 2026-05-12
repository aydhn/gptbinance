import pytest
from app.observability_plane.gaps import GapDetectorRegistry
from app.observability_plane.models import TelemetryGapFinding

def test_gap_reporting():
    reg = GapDetectorRegistry()
    reg.report_gap(TelemetryGapFinding(gap_id="g1", missing_telemetry_id="t1", blast_radius="high"))
    assert reg.get_gap("g1").missing_telemetry_id == "t1"
