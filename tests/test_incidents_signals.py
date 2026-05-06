import pytest
from app.incidents.signals import SignalMapper
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity


def test_signals():
    sig = SignalMapper.create_signal(
        signal_id="sig-1",
        signal_type=SignalType.MARKET_TRUTH_BROKEN,
        domain="market_truth",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref="BTCUSDT",
        severity=IncidentSeverity.CRITICAL_INCIDENT,
    )
    assert sig.signal_id == "sig-1"
    assert sig.type == SignalType.MARKET_TRUTH_BROKEN
