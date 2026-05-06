import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository
from app.incidents.policies import IncidentPolicyChecker


def test_policies():
    repo = IncidentRepository(IncidentStorage(".test_incidents_policies"))
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

    blockers = IncidentPolicyChecker.block_recovery(inc)
    assert len(blockers) > 0

    # cleanup
    import shutil

    shutil.rmtree(".test_incidents_policies", ignore_errors=True)
