import pytest
from app.observability_plane.diagnostics import DiagnosticSignalBuilder
from app.observability_plane.models import DiagnosticSignal
from app.observability_plane.enums import DiagnosticClass

def test_diagnostic_signals():
    builder = DiagnosticSignalBuilder()
    builder.register_signal(DiagnosticSignal(signal_id="s1", diagnostic_class=DiagnosticClass.SYMPTOM, contributing_telemetry=["t1"]))
    assert builder.get_signal("s1").diagnostic_class == DiagnosticClass.SYMPTOM
