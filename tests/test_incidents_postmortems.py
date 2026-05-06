import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity


def test_postmortem_seed():
    cmd = IncidentCommand()
    sig = IncidentSignal(
        signal_id="sig-1",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt",
        scope_type=IncidentScopeType.GLOBAL,
        scope_ref="GLOBAL",
        severity_hint=IncidentSeverity.CRITICAL_INCIDENT,
    )
    inc = cmd.ingest_signal(sig)
    assert inc.postmortem_seed is not None
    assert len(inc.postmortem_seed.frozen_evidence_refs) == 1
