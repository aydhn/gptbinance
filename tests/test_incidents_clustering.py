import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository

def test_clustering():
    repo = IncidentRepository(IncidentStorage(".test_incidents_clustering"))
    cmd = IncidentCommand(repo)
    sig1 = IncidentSignal(
        signal_id="sig-1",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="market_truth",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT",
        severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    sig2 = IncidentSignal(
        signal_id="sig-2",
        type=SignalType.CROSS_BOOK_CONFLICT,
        source_domain="cross_book",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT",
        severity_hint=IncidentSeverity.MAJOR_INCIDENT
    )
    inc1 = cmd.ingest_signal(sig1)
    inc2 = cmd.ingest_signal(sig2)
    assert inc1.incident_id == inc2.incident_id
    assert len(inc2.signals) == 2

    # cleanup
    import shutil
    shutil.rmtree(".test_incidents_clustering", ignore_errors=True)
