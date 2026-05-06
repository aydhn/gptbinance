import pytest
from app.incidents.intake import IncidentCommand
from app.incidents.models import IncidentSignal
from app.incidents.enums import SignalType, IncidentScopeType, IncidentSeverity
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository
from app.incidents.evidence import EvidenceManager


def test_evidence():
    repo = IncidentRepository(IncidentStorage(".test_incidents_evidence"))
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

    mgr = EvidenceManager(repo)
    bundle = mgr.get_evidence_bundle(inc.incident_id)

    assert "snapshots" in bundle
    assert "signals" in bundle
    assert "sig-1" in bundle["signals"]

    # cleanup
    import shutil

    shutil.rmtree(".test_incidents_evidence", ignore_errors=True)
