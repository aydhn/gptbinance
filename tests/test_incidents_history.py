import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository
from app.incidents.history import IncidentHistoryManager

def test_history():
    repo = IncidentRepository(IncidentStorage(".test_incidents_history"))
    cmd = IncidentCommand(repo)
    sig1 = IncidentSignal(
        signal_id="sig-1", type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt", scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT", severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    sig2 = IncidentSignal(
        signal_id="sig-2", type=SignalType.CROSS_BOOK_CONFLICT,
        source_domain="cb", scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT", severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    cmd.ingest_signal(sig1)
    cmd.ingest_signal(sig2)

    mgr = IncidentHistoryManager(repo)
    clusters = mgr.get_repeated_clusters()

    # They should cluster into a single incident due to same scope
    assert len(clusters) == 0

    # cleanup
    import shutil
    shutil.rmtree(".test_incidents_history", ignore_errors=True)
