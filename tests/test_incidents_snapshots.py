import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository


def test_snapshots():
    repo = IncidentRepository(IncidentStorage(".test_incidents_snapshots"))
    cmd = IncidentCommand(repo)
    sig = IncidentSignal(
        signal_id="sig-1",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt",
        scope_type=IncidentScopeType.GLOBAL,
        scope_ref="GLOBAL",
        severity_hint=IncidentSeverity.CRITICAL_INCIDENT,
    )
    inc = cmd.ingest_signal(sig)

    assert len(inc.snapshots) == 1
    assert inc.snapshots[0].is_complete == True

    # cleanup
    import shutil

    shutil.rmtree(".test_incidents_snapshots", ignore_errors=True)
