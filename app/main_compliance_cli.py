import argparse
import sys
from app.compliance_plane.repository import ComplianceRepository
from app.compliance_plane.requirements import create_requirement
from app.compliance_plane.enums import RequirementClass


def setup_dummy_data(repo: ComplianceRepository):
    req = create_requirement(
        req_id="REQ-ACC-001",
        req_class=RequirementClass.ACCESS_CONTROL,
        scope={"env": "all"},
        owner_id="sysadmin",
        satisfaction_criteria="All critical actions are dual-approved.",
        review_cadence_days=90,
        failure_severity="critical",
        lineage_refs=[],
        is_mandatory=True,
    )
    repo.registry.register_requirement(req)


def main():
    parser = argparse.ArgumentParser(description="Compliance Plane CLI")
    parser.add_argument(
        "--show-compliance-registry", action="store_true", help="Show registry summary"
    )
    parser.add_argument(
        "--show-requirement",
        type=str,
        help="Show requirement details by ID",
        metavar="<id>",
    )
    parser.add_argument(
        "--show-control-objectives", action="store_true", help="Show control objectives"
    )
    parser.add_argument(
        "--show-control-mappings", action="store_true", help="Show control mappings"
    )
    parser.add_argument(
        "--show-evidence-requirements",
        action="store_true",
        help="Show evidence requirements",
    )
    parser.add_argument(
        "--show-retention-policies", action="store_true", help="Show retention policies"
    )
    parser.add_argument(
        "--show-attestations", action="store_true", help="Show attestations"
    )
    parser.add_argument(
        "--show-certifications", action="store_true", help="Show certifications"
    )
    parser.add_argument(
        "--show-control-effectiveness",
        action="store_true",
        help="Show control effectiveness reviews",
    )
    parser.add_argument(
        "--show-compliance-exceptions",
        action="store_true",
        help="Show compliance exceptions",
    )
    parser.add_argument(
        "--show-compensating-controls",
        action="store_true",
        help="Show compensating controls",
    )
    parser.add_argument(
        "--show-audit-readiness",
        action="store_true",
        help="Show audit readiness report",
    )
    parser.add_argument(
        "--show-compliance-findings",
        action="store_true",
        help="Show compliance findings",
    )
    parser.add_argument(
        "--show-compliance-remediation",
        action="store_true",
        help="Show compliance remediations",
    )
    parser.add_argument(
        "--show-compliance-debt", action="store_true", help="Show compliance debt"
    )
    parser.add_argument(
        "--show-compliance-recurrence",
        action="store_true",
        help="Show compliance recurrence records",
    )
    parser.add_argument(
        "--show-compliance-equivalence",
        action="store_true",
        help="Show compliance equivalence reports",
    )
    parser.add_argument(
        "--show-compliance-trust",
        action="store_true",
        help="Show compliance trust verdict",
    )
    parser.add_argument(
        "--show-compliance-review-packs",
        action="store_true",
        help="Show compliance review packs",
    )

    args = parser.parse_args()

    repo = ComplianceRepository()
    setup_dummy_data(repo)

    if args.show_compliance_registry:
        reqs = repo.registry.list_requirements()
        ctrls = repo.registry.list_controls()
        print(f"Compliance Registry:")
        print(f"  Requirements: {len(reqs)}")
        print(f"  Controls: {len(ctrls)}")
        for r in reqs:
            print(
                f"  - [{r.requirement_class.value}] {r.requirement_id}: {r.satisfaction_criteria}"
            )
        sys.exit(0)

    if args.show_requirement:
        req = repo.registry.get_requirement(args.show_requirement)
        if req:
            print(f"Requirement: {req.requirement_id}")
            print(f"  Class: {req.requirement_class.value}")
            print(f"  Owner: {req.owner_id}")
            print(f"  Scope: {req.scope}")
            print(f"  Criteria: {req.satisfaction_criteria}")
        else:
            print(f"Requirement '{args.show_requirement}' not found.")
        sys.exit(0)

    # Simplified handlers for demonstration.
    # In a real scenario, these would iterate over the repository's data and print formatted output.
    commands = [
        "show_control_objectives",
        "show_control_mappings",
        "show_evidence_requirements",
        "show_retention_policies",
        "show_attestations",
        "show_certifications",
        "show_control_effectiveness",
        "show_compliance_exceptions",
        "show_compensating_controls",
        "show_audit_readiness",
        "show_compliance_findings",
        "show_compliance_remediation",
        "show_compliance_debt",
        "show_compliance_recurrence",
        "show_compliance_equivalence",
        "show_compliance_trust",
        "show_compliance_review_packs",
    ]

    for cmd in commands:
        if getattr(args, cmd, False):
            print(f"Executing: {cmd.replace('_', '-')} (No data loaded in mock)")
            sys.exit(0)


if __name__ == "__main__":
    main()
