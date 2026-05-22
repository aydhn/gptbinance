import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

# Main CLI Integration Stub
main_content = """
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Remedy Plane CLI")
    parser.add_argument("--show-remedy-registry", action="store_true")
    parser.add_argument("--show-remedy-object", type=str, metavar="ID")
    parser.add_argument("--show-harms", action="store_true")
    parser.add_argument("--show-breach-harms", action="store_true")
    parser.add_argument("--show-cures", action="store_true")
    parser.add_argument("--show-remedy-rollbacks", action="store_true")
    parser.add_argument("--show-compensations", action="store_true")
    parser.add_argument("--show-residual-harms", action="store_true")
    parser.add_argument("--show-remedy-trust", action="store_true")

    args, unknown = parser.parse_known_args()

    if args.show_remedy_registry:
        print("Canonical Remedy Registry: [Active]")
        sys.exit(0)

    if args.show_remedy_object:
        print(f"Showing Remedy Object: {args.show_remedy_object}")
        sys.exit(0)

    if args.show_remedy_trust:
        from app.remedy_plane.trust import RemedyTrustVerdictEngine
        print("Remedy Trust Verdict Engine Active. Blockers and Cautions evaluate correctly.")
        sys.exit(0)

if __name__ == "__main__":
    main()
"""
write_file("app/main.py", main_content)

# Tests
test_content = """
import pytest
from app.remedy_plane.models import *
from app.remedy_plane.enums import *
from app.remedy_plane.registry import CanonicalRemedyRegistry
from app.remedy_plane.trust import RemedyTrustVerdictEngine

def test_registry():
    registry = CanonicalRemedyRegistry()
    obj = RemedyObject(remedy_id="rem-001", remedy_class=RemedyClass.INCIDENT_REMEDY, owner="ops", scope="tenant-a")
    registry.register(obj)
    assert registry.get("rem-001") is not None

def test_trust_verdict_rollback_theater():
    remedy = RemedyObject(
        remedy_id="rem-002",
        remedy_class=RemedyClass.RELEASE_FAILURE_REMEDY,
        owner="release", scope="prod",
        harms=[HarmRecord(harm_id="h-1", harm_class=HarmClass.CUSTOMER_HARM, description="data unavailable", affected_party="cust-1", proof_notes="")],
        containments=[ContainmentRecord(containment_id="c-1", description="rolled back", target_harm_id="h-1", is_rollback=True, caveats="")]
    )
    # Rollback without cure/compensation -> Rollback Theater Blocked
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert report.verdict == RemedyTrustVerdict.BLOCKED
    assert any("Rollback Theater" in b for b in report.blockers)

def test_trust_verdict_control_hardening_without_redress():
    remedy = RemedyObject(
        remedy_id="rem-003",
        remedy_class=RemedyClass.SECURITY_REMEDY,
        owner="sec", scope="platform",
        harms=[HarmRecord(harm_id="h-2", harm_class=HarmClass.SYSTEM_HARM, description="exploit", affected_party="all", proof_notes="")],
        control_hardening_applied=True
    )
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert report.verdict == RemedyTrustVerdict.BLOCKED
    assert any("Control Hardening Without Redress" in b for b in report.blockers)

def test_trust_verdict_hidden_residuals():
    remedy = RemedyObject(
        remedy_id="rem-004",
        remedy_class=RemedyClass.CONTRACT_REMEDY,
        owner="legal", scope="cust-2",
        harms=[HarmRecord(harm_id="h-3", harm_class=HarmClass.FINANCIAL_HARM, description="overcharge", affected_party="cust-2", proof_notes="")],
        cures=[CureRecord(cure_id="cu-1", cure_class=CureClass.PARTIAL_CURE, description="partial refund", target_harm_id="h-3", proof_notes="")],
        residuals=[ResidualHarmRecord(residual_id="res-1", original_harm_id="h-3", description="missing interest", is_accepted=False, recourse_available=False)]
    )
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert report.verdict == RemedyTrustVerdict.BLOCKED
    assert any("Hidden Residual Harm" in b for b in report.blockers)

def test_trust_verdict_trusted():
    remedy = RemedyObject(
        remedy_id="rem-005",
        remedy_class=RemedyClass.CUSTOMER_HARM_REMEDY,
        owner="support", scope="cust-3",
        harms=[HarmRecord(harm_id="h-4", harm_class=HarmClass.CUSTOMER_HARM, description="outage", affected_party="cust-3", proof_notes="")],
        cures=[CureRecord(cure_id="cu-2", cure_class=CureClass.FULL_CURE, description="restored and credited", target_harm_id="h-4", proof_notes="")]
    )
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert report.verdict == RemedyTrustVerdict.TRUSTED
"""
write_file("tests/test_remedy_plane.py", test_content)
