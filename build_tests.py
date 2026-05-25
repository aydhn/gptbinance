import os
with open("tests/test_performance_security_plane.py", "w") as f:
    f.write("""
import pytest
from datetime import datetime
from app.performance_security_plane.registry import CanonicalPerformanceSecurityRegistry
from app.performance_security_plane.models import PerformanceSecurityObject, FundingStatusRecord, DrawRightRecord
from app.performance_security_plane.enums import SecurityClass, FundingClass, DrawClass, TrustVerdict
from app.performance_security_plane.trust import TrustedPerformanceSecurityVerdictEngine
from app.settlement_plane.performance import evaluate_performance_security_integration as eval_settlement
from app.contract_plane.consumer_impact import evaluate_performance_security_integration as eval_contract
from app.federation_plane.verdicts import evaluate_performance_security_integration as eval_federation
from app.observability_plane.events import evaluate_performance_security_integration as eval_observability

def test_security_registry_integrity():
    registry = CanonicalPerformanceSecurityRegistry()
    obj = PerformanceSecurityObject(
        security_id="SEC-001",
        owner_id="OWNER-1",
        security_class=SecurityClass.ESCROW,
        scope="milestone",
        created_at=datetime.utcnow()
    )
    registry.register(obj)
    fetched = registry.get("SEC-001")
    assert fetched is not None
    assert fetched.security_class == SecurityClass.ESCROW

def test_trust_verdict_engine():
    engine = TrustedPerformanceSecurityVerdictEngine()

    funding = FundingStatusRecord(security_id="SEC-001", funding_class=FundingClass.UNFUNDED, amount=100.0, currency="USD")
    draw = DrawRightRecord(security_id="SEC-001", draw_class=DrawClass.IMMEDIATE, beneficiary_id="BEN-1", conditions=[])

    verdict = engine.evaluate("SEC-001", funding, draw)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert any("Material undersecurity detected: Unfunded security" in b for b in verdict.blockers)

def test_settlement_integration_caution():
    class MockRecords:
        is_unfunded = True
    cautions = eval_settlement({}, MockRecords())
    assert any("structured settlement performance marked safe without security posture explicit caution üretsin" in c for c in cautions)

def test_contract_integration():
    class MockRecords:
        is_unfunded = True
    cautions = eval_contract({}, MockRecords())
    assert any("consumer impact closed under cosmetic security explicit caution üretsin" in c for c in cautions)

def test_federated_gap():
    class MockRecords:
        is_unfunded = True
    cautions = eval_federation({}, MockRecords())
    assert any("federated safe verdict under orphaned beneficiary draw right blocker/caution üretsin" in c for c in cautions)

""")
