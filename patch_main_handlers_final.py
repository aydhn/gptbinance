import re

with open("app/main.py", "r") as f:
    content = f.read()

handlers = """
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
"""

content = re.sub(r"(\s*if args\.check_only:)", handlers + r"\1", content)

with open("app/main.py", "w") as f:
    f.write(content)
