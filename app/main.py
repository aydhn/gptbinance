import sys
import json
from datetime import datetime, timezone
from app.operating_model_plane.registry import CanonicalOperatingModelRegistry
from app.operating_model_plane.models import OperatingModelObject, RoleRef, OwnershipAssignment
from app.operating_model_plane.enums import OperatingObjectClass, RoleClass, OwnershipClass, CoverageClass

def build_dummy_registry():
    registry = CanonicalOperatingModelRegistry()
    role = RoleRef(role_id="r1", role_name="Trading Core Lead", role_class=RoleClass.ACCOUNTABLE_OWNER)
    owner = OwnershipAssignment(
        assignment_id="a1",
        target_id="surf_1",
        owner_role=role,
        ownership_class=OwnershipClass.PRIMARY,
        last_attested_at=datetime.now(timezone.utc)
    )
    obj = OperatingModelObject(
        operating_id="surf_1",
        object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True,
        primary_owner=owner,
        backup_coverage=CoverageClass.ON_CALL_24_7,
        escalation_chain=None
    )
    registry.register(obj)
    return registry

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python -m app.main [command]")
        return

    registry = build_dummy_registry()

    cmd = args[0]
    if cmd == "--show-operating-model-registry":
        print(json.dumps([o.dict() for o in registry.get_all()], indent=2, default=str))
    elif cmd == "--show-operating-object":
        print(f"Showing object {args[2]}...")
    elif cmd == "--show-role-definitions":
        print("Role definitions (Accountable, Responsible, Reviewer, Approver, Escalation)...")
    elif cmd == "--show-ownership-assignments":
        print("Ownership Assignments (Primary, Freshness, Warnings)...")
    elif cmd == "--show-sod":
        print("Segregation of Duties (Propose/Approve, Execute/Review) Violations...")
    elif cmd == "--show-operating-trust":
        from app.operating_model_plane.trust import OperatingModelTrustEngine
        engine = OperatingModelTrustEngine()
        res = engine.evaluate(registry.get_all()[0])
        print(json.dumps(res.dict(), indent=2, default=str))

    elif cmd == "--show-knowledge-registry":
        print("Knowledge Registry: [Active]")
    elif cmd == "--show-knowledge-object":
        print(f"Knowledge Object: {args[2] if len(args) > 2 else 'Unknown'}")
    elif cmd == "--show-knowledge-taxonomy":
        print("Knowledge Taxonomy: [Policy, Standard, SOP, Checklist, Runbook, Playbook, Architecture Note, Decision Memo, Troubleshooting Note]")
    elif cmd == "--show-knowledge-sources":
        print("Knowledge Sources: [Canonical, Mirrored, Superseded, Local, Generated]")
    elif cmd == "--show-standards":
        print("Knowledge Standards: [Mandatory, Advisory]")
    elif cmd == "--show-runbooks":
        print("Knowledge Runbooks: [Incident, Release Rollback, Failover, Operational Recovery]")
    elif cmd == "--show-playbooks":
        print("Knowledge Playbooks: [Escalation, Security Response, Release Management, Migration, Staged Execution]")
    elif cmd == "--show-sops":
        print("Knowledge SOPs: [Workflow, Review, Compliance, Data/Model Change, Operator]")
    elif cmd == "--show-knowledge-checklists":
        print("Knowledge Checklists: [Release, Activation, Incident, Compliance Evidence, Readiness]")
    elif cmd == "--show-knowledge-applicability":
        print("Knowledge Applicability: [Environment, Role, Workflow, Release Stage, Incident Severity]")
    elif cmd == "--show-knowledge-freshness":
        print("Knowledge Freshness: [Fresh, Review Due, Stale, Expired]")
    elif cmd == "--show-knowledge-reviews":
        print("Knowledge Reviews: [Scheduled, Triggered, Incident-Triggered, Release-Triggered]")
    elif cmd == "--show-knowledge-supersession":
        print("Knowledge Supersession: [Superseded, Replacement Chain, Partial Supersession, Blocked Supersession]")
    elif cmd == "--show-knowledge-conflicts":
        print("Knowledge Conflicts: [Conflicting Standards, Conflicting Runbooks, Overlapping Checklists, Role-Conflicting Procedures]")
    elif cmd == "--show-knowledge-adoption":
        print("Knowledge Adoption: [Workflow, Release, Team, Operator]")
    elif cmd == "--show-knowledge-attestations":
        print("Knowledge Attestations: [Read-and-Understood, Review-Complete, Drill-Proven, Control-Attached]")
    elif cmd == "--show-knowledge-retrieval":
        print("Knowledge Retrieval: [Authoritative, Advisory, Conflicting, Stale]")
    elif cmd == "--show-knowledge-usability":
        print("Knowledge Usability: [Actionable Runbook, Step Clarity, Prereq Completeness, Recovery Usability]")
    elif cmd == "--show-knowledge-coverage":
        print("Knowledge Coverage: [Critical Surface, Release, Incident, Continuity/Security/Compliance, Owner-Role]")
    elif cmd == "--show-knowledge-gaps":
        print("Knowledge Gaps: [Missing Runbook, Missing Checklist, Missing Standard, Missing Role Guidance, Missing Acceptance Guidance]")
    elif cmd == "--show-knowledge-forecast":
        print("Knowledge Forecast: [Freshness Decay, Review Backlog, Supersession Drift, Adoption Lag, Gap Growth]")
    elif cmd == "--show-knowledge-debt":
        print("Knowledge Debt: [Stale Doc, Orphan Runbook, Superseded-Reference, Conflicting Guidance, Unadopted Standard]")
    elif cmd == "--show-knowledge-equivalence":
        print("Knowledge Equivalence: [Replay/Paper/Probation/Live]")
    elif cmd == "--show-knowledge-trust":
        print("Knowledge Trust: [Trusted, Caution, Degraded, Blocked, Review Required]")
    elif cmd == "--show-knowledge-review-packs":
        print("Knowledge Review Packs: [Integrity, Freshness/Supersession, Runbook/Checklist Usability, Applicability/Conflict]")
    elif cmd == "--show-assurance-registry":
        print("Assurance Registry: Displaying canonical controls and objectives...")
    elif cmd == "--show-assurance-object":
        print(f"Showing assurance object {args[1] if len(args) > 1 else 'Unknown'}...")
    elif cmd == "--show-controls":
        print("Controls: Preventive, Detective, Corrective, Governance, Operational...")
    elif cmd == "--show-control-objectives":
        print("Control Objectives: Objectives, Scope, Risk Alignment, Sufficiency Notes...")
    elif cmd == "--show-assurance-evidence":
        print("Assurance Evidence: Runtime, Review, Drill, Checklist, Recency...")
    elif cmd == "--show-design-effectiveness":
        print("Design Effectiveness: Design Completeness, Dependency Sufficiency, Caveats...")
    elif cmd == "--show-operating-effectiveness":
        print("Operating Effectiveness: Sustained/Degraded, Evidence-Backed Status...")
    elif cmd == "--show-assurance-tests":
        print("Assurance Tests: Walkthrough, Scenario, Negative, Effectiveness, Scope...")
    elif cmd == "--show-assurance-samples":
        print("Assurance Samples: Sampling Plans, Population Coverage, Adequacy...")
    elif cmd == "--show-assurance-attestations":
        print("Assurance Attestations: Owner, Reviewer, Independent, Drill-Backed...")
    elif cmd == "--show-assurance-findings":
        print("Assurance Findings: Design/Operating/Stale/Independence Findings, Severity...")
    elif cmd == "--show-assurance-exceptions":
        print("Assurance Exceptions: Scoped Exceptions, Expiry, Residual Risk...")
    elif cmd == "--show-assurance-remediation":
        print("Assurance Remediation: Paths, Ownership, Sufficiency, Stalled Surfaces...")
    elif cmd == "--show-assurance-closure":
        print("Assurance Closure: Partial/Verified Closures, Premature Warnings...")
    elif cmd == "--show-assurance-coverage":
        print("Assurance Coverage: Control/Plane/High-Risk Coverage, Blind Spots...")
    elif cmd == "--show-assurance-independence":
        print("Assurance Independence: Reviewer/Tester/Approver Independence, Same-Chain Caveats...")
    elif cmd == "--show-assurance-schedules":
        print("Assurance Schedules: Periodic/Triggered/Release/Incident Schedules, Overdue...")
    elif cmd == "--show-assurance-gaps":
        print("Assurance Gaps: Missing Controls/Evidence/Tests/Independent Review, Severity...")
    elif cmd == "--show-assurance-forecast":
        print("Assurance Forecast: Staleness, Finding Accumulation, Degradation...")
    elif cmd == "--show-assurance-debt":
        print("Assurance Debt: Stale Evidence, Expired Exceptions, Repeated Failures...")
    elif cmd == "--show-assurance-equivalence":
        print("Assurance Equivalence: Replay/Paper/Probation/Live Verdict and Blockers...")
    elif cmd == "--show-assurance-trust":
        print("Assurance Trust: Trusted Posture, Blockers, Caveats...")
    elif cmd == "--show-assurance-review-packs":
        print("Assurance Review Packs: Evidence/Testing/Finding-Closure Packs...")
    else:
        print(f"Command {cmd} acknowledged (Implementation stub for Operating Model Plane).")

if __name__ == "__main__":
    main()
