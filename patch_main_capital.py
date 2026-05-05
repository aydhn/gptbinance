import re

with open("app/main.py", "r") as f:
    content = f.read()

# Add imports if not present
if "from app.capital.reporting" not in content:
    imports = """
from app.capital.reporting import (
    report_ladder_summary,
    report_posture,
    report_escalation_check,
    report_reduction_check,
    report_budgets,
    report_evidence,
    report_transition_plan
)
from app.capital.repository import capital_repository
from app.capital.freeze import freeze_manager
from app.capital.tranches import tranche_manager
from app.control.actions import ActionRegistry, SensitiveAction
"""
    # Insert right after other app. imports
    content = re.sub(r"(from app\.[^\n]+)", r"\1\n" + imports, content, count=1)

# Add CLI arguments
arg_pattern = r'parser\.add_argument\("--run-workspaces-tests", action="store_true"\)'
capital_args = """    parser.add_argument("--run-workspaces-tests", action="store_true")
    # Capital Governance Commands
    parser.add_argument("--show-capital-ladder", action="store_true", help="Show defined tiers, tranches and transitions")
    parser.add_argument("--show-capital-posture", action="store_true", help="Show current active tier and budget usage")
    parser.add_argument("--run-capital-escalation-check", type=str, help="Run escalation readiness check against target tier", metavar="TARGET_TIER")
    parser.add_argument("--run-capital-reduction-check", action="store_true", help="Run reduce/freeze advisory check based on loss/stress posture")
    parser.add_argument("--show-capital-budgets", action="store_true", help="Show specific budgets for the active tier")
    parser.add_argument("--show-capital-evidence", action="store_true", help="Show current evidence bundle completeness and freshness")
    parser.add_argument("--show-capital-transition-plan", type=str, help="Show dry-run transition plan to target tier", metavar="TARGET_TIER")
    parser.add_argument("--request-capital-tier-change", type=str, help="Create a sensitive action request for tier change", metavar="TARGET_TIER")
    parser.add_argument("--show-capital-freeze-state", action="store_true", help="Show current freeze status, reasons and thaw prerequisites")
    parser.add_argument("--show-tranche-status", action="store_true", help="Show active/inactive tranches and activation history")
"""

if "--show-capital-ladder" not in content:
    content = content.replace(
        'parser.add_argument("--run-workspaces-tests", action="store_true")',
        capital_args,
    )
    if capital_args not in content:  # If replace failed
        # Try appending to argument list
        content = re.sub(
            r"(parser\.parse_args\(\))", capital_args + r"\n    \1", content
        )


# Add command handlers in main()
handlers_pattern = r"if args\.show_telemetry_digest:"

capital_handlers = """if args.show_capital_ladder:
        print(report_ladder_summary())
        return

    if args.show_capital_posture:
        active_tier = capital_repository.get_current_tier().tier_id
        # Simulated usage data for CLI
        usage = {"total_deployed": 10.0, "total_reserved": 5.0, "total_frozen": 0.0, "concurrent_positions": 1, "loss_intraday": 2.0}
        print(report_posture(active_tier, usage))
        return

    if args.run_capital_escalation_check:
        active_tier = capital_repository.get_current_tier().tier_id
        usage = {"total_deployed": 10.0}
        print(report_escalation_check(active_tier, args.run_capital_escalation_check, usage))
        return

    if args.run_capital_reduction_check:
        active_tier = capital_repository.get_current_tier().tier_id
        usage = {"total_deployed": 10.0, "loss_intraday": 100.0} # Simulate high loss
        print(report_reduction_check(active_tier, usage))
        return

    if args.show_capital_budgets:
        active_tier = capital_repository.get_current_tier().tier_id
        print(report_budgets(active_tier))
        return

    if args.show_capital_evidence:
        print(report_evidence())
        return

    if args.show_capital_transition_plan:
        active_tier = capital_repository.get_current_tier().tier_id
        print(report_transition_plan(active_tier, args.show_capital_transition_plan))
        return

    if args.request_capital_tier_change:
        print(f"Creating sensitive action request for tier change to: {args.request_capital_tier_change}")
        from app.control.actions import SensitiveAction
        import uuid
        action = SensitiveAction(
            action_id=f"cap_req_{uuid.uuid4().hex[:8]}",
            action_type="capital_tier_change",
            parameters={"target_tier": args.request_capital_tier_change},
            requested_by="cli_operator",
            criticality="high",
            approval_requirement=["governance_capital_committee"]
        )
        print(f"Action Request Created: {action.action_id}")
        print(f"Approvals Required: {action.approval_requirement}")
        return

    if args.show_capital_freeze_state:
        state = freeze_manager.get_state()
        print(f"Capital Freeze State")
        print("-" * 40)
        print(f"Status: {state.status.value}")
        print(f"Reasons: {state.reasons}")
        print(f"Thaw Prerequisites: {state.thaw_prerequisites}")
        return

    if args.show_tranche_status:
        active = tranche_manager.get_active_tranches()
        print(f"Tranche Status")
        print("-" * 40)
        print(f"Active Tranches: {len(active)}")
        for t in active:
            print(f" - {t.tranche_id} (Activated: {t.activated_at.isoformat()})")
        return

    if args.show_telemetry_digest:"""

if "args.show_capital_ladder" not in content:
    content = content.replace("if args.show_telemetry_digest:", capital_handlers)

with open("app/main.py", "w") as f:
    f.write(content)
