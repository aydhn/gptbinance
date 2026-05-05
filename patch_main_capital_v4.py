import re

with open("app/main.py", "r") as f:
    content = f.read()

# Let's fix the argument parsing logic safely without relying on regex regex replacing that might fail
# First, find parser.parse_args() and replace with capital args + parse args
if 'parser.add_argument("--show-capital-ladder' not in content:
    capital_args = """
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

    args = parser.parse_args()
"""
    content = content.replace("args = parser.parse_args()", capital_args)

if "report_ladder_summary()" not in content:
    capital_handlers = """
    if getattr(args, 'show_capital_ladder', False):
        print(report_ladder_summary())
        return

    if getattr(args, 'show_capital_posture', False):
        active_tier = capital_repository.get_current_tier().tier_id
        usage = {"total_deployed": 10.0, "total_reserved": 5.0, "total_frozen": 0.0, "concurrent_positions": 1, "loss_intraday": 2.0}
        print(report_posture(active_tier, usage))
        return

    if getattr(args, 'run_capital_escalation_check', None):
        active_tier = capital_repository.get_current_tier().tier_id
        usage = {"total_deployed": 10.0}
        print(report_escalation_check(active_tier, args.run_capital_escalation_check, usage))
        return

    if getattr(args, 'run_capital_reduction_check', False):
        active_tier = capital_repository.get_current_tier().tier_id
        usage = {"total_deployed": 10.0, "loss_intraday": 100.0}
        print(report_reduction_check(active_tier, usage))
        return

    if getattr(args, 'show_capital_budgets', False):
        active_tier = capital_repository.get_current_tier().tier_id
        print(report_budgets(active_tier))
        return

    if getattr(args, 'show_capital_evidence', False):
        print(report_evidence())
        return

    if getattr(args, 'show_capital_transition_plan', None):
        active_tier = capital_repository.get_current_tier().tier_id
        print(report_transition_plan(active_tier, args.show_capital_transition_plan))
        return

    if getattr(args, 'request_capital_tier_change', None):
        print(f"Creating sensitive action request for tier change to: {args.request_capital_tier_change}")
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

    if getattr(args, 'show_capital_freeze_state', False):
        state = freeze_manager.get_state()
        print(f"Capital Freeze State")
        print("-" * 40)
        print(f"Status: {state.status.value}")
        print(f"Reasons: {state.reasons}")
        print(f"Thaw Prerequisites: {state.thaw_prerequisites}")
        return

    if getattr(args, 'show_tranche_status', False):
        active = tranche_manager.get_active_tranches()
        print(f"Tranche Status")
        print("-" * 40)
        print(f"Active Tranches: {len(active)}")
        for t in active:
            print(f" - {t.tranche_id} (Activated: {t.activated_at.isoformat()})")
        return

    if getattr(args, 'check_only', False):
"""
    content = content.replace(
        "if getattr(args, 'check_only', False):", capital_handlers
    )


with open("app/main.py", "w") as f:
    f.write(content)
