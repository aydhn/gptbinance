import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository

def test_timeline():
    repo = IncidentRepository(IncidentStorage(".test_incidents_timeline"))
    cmd = IncidentCommand(repo)
    sig = IncidentSignal(
        signal_id="sig-1", type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt", scope_type=IncidentScopeType.GLOBAL,
        scope_ref="GLOBAL", severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    inc = cmd.ingest_signal(sig)

    assert len(inc.timeline) > 0
    assert inc.timeline[0].event_type == "INCIDENT_OPENED"

    # cleanup
    import shutil
    shutil.rmtree(".test_incidents_timeline", ignore_errors=True)
