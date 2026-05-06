import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import (
    SignalType,
    IncidentScopeType,
    IncidentSeverity,
    DegradedModeType,
)
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository


def test_degraded_modes():
    repo = IncidentRepository(IncidentStorage(".test_incidents_degraded"))
    cmd = IncidentCommand(repo)
    sig = IncidentSignal(
        signal_id="sig-1",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT",
        severity_hint=IncidentSeverity.CRITICAL_INCIDENT,
    )
    inc = cmd.ingest_signal(sig)
    assert inc.degraded_mode_plan is not None
    assert inc.degraded_mode_plan.mode == DegradedModeType.PAPER_SHADOW_ONLY

    # cleanup
    import shutil

    shutil.rmtree(".test_incidents_degraded", ignore_errors=True)
