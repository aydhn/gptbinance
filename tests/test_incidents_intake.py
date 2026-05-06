import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity

def test_intake_creates_incident():
    cmd = IncidentCommand()
    sig = IncidentSignal(
        signal_id="sig-1",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="market_truth",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT",
        severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    inc = cmd.ingest_signal(sig)
    assert inc is not None
    assert inc.severity == IncidentSeverity.CRITICAL_INCIDENT
    assert len(inc.snapshots) == 1
    assert inc.containment_plan is not None
