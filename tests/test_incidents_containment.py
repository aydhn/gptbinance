import pytest
from app.incidents.containment import ContainmentPlanner
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity, ContainmentIntentType

def test_containment_advisory():
    cmd = IncidentCommand()
    sig = IncidentSignal(
        signal_id="sig-1", type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="mkt", scope_type=IncidentScopeType.GLOBAL,
        scope_ref="GLOBAL", severity_hint=IncidentSeverity.CRITICAL_INCIDENT
    )
    inc = cmd.ingest_signal(sig)
    assert inc.containment_plan.intent == ContainmentIntentType.GLOBAL_HALT_ADVISORY
