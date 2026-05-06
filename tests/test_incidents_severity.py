import pytest
from app.incidents.severity import SeverityMatrix
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType

def test_severity_matrix():
    sig = IncidentSignal(
        signal_id="sig-2",
        type=SignalType.MARKET_TRUTH_BROKEN,
        source_domain="market",
        scope_type=IncidentScopeType.GLOBAL,
        scope_ref="*",
        severity_hint=IncidentSeverity.WARNING
    )
    sev = SeverityMatrix.evaluate_initial(sig)
    assert sev == IncidentSeverity.CRITICAL_INCIDENT
