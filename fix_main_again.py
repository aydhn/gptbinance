import sys

with open('app/main.py', 'r') as f:
    content = f.read()

assurance_commands = """    elif cmd == "--show-assurance-registry":
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
        print(f"Command {cmd} acknowledged (Implementation stub for Operating Model Plane).")"""

if "--show-assurance-registry" not in content:
    content = content.replace('    else:\n        print(f"Command {cmd} acknowledged (Implementation stub for Operating Model Plane).")', assurance_commands)

with open('app/main.py', 'w') as f:
    f.write(content)
