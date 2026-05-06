import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity, RecoveryVerdict
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository

def test_recovery_gates():
    repo = IncidentRepository(IncidentStorage(".test_incidents_recovery"))
    cmd = IncidentCommand(repo)
    sig = IncidentSignal(
        signal_id="sig-1", type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt", scope_type=IncidentScopeType.GLOBAL,
        scope_ref="GLOBAL", severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    inc = cmd.ingest_signal(sig)
    assert inc.recovery_plan.verdict == RecoveryVerdict.NOT_READY

    cmd.mark_contained(inc.incident_id)
    inc = repo.get(inc.incident_id)
    assert inc.recovery_plan.verdict == RecoveryVerdict.CONDITIONAL

    # cleanup
    import shutil
    shutil.rmtree(".test_incidents_recovery", ignore_errors=True)
