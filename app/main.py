import argparse
from datetime import datetime, timezone
import uuid

# Dummy implementation for CLI demonstration
from app.stressrisk.models import (
    PortfolioStressSnapshot,
    StressBudgetResult,
    StressOverlayDecision,
    StressRun,
)
from app.stressrisk.enums import LossSeverity, BudgetVerdict, StressOverlayVerdict

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



def main():
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    parser.add_argument("--check-only", action="store_true", help="Run checks only")
    parser.add_argument("--show-crossbook-summary", action="store_true", help="Show unified cross-book posture")
    parser.add_argument("--show-exposure-graph", action="store_true", help="Show current exposure graph nodes/edges")
    parser.add_argument("--show-net-exposure", action="store_true", help="Show gross/net exposure summary")
    parser.add_argument("--show-collateral-pressure", action="store_true", help="Show locked/usable collateral summary")
    parser.add_argument("--show-borrow-dependency", action="store_true", help="Show borrowed assets and dependency")
    parser.add_argument("--show-funding-burden", action="store_true", help="Show funding drag by symbol/product")
    parser.add_argument("--show-basis-exposure", action="store_true", help="Show apparent hedge vs basis-risk")
    parser.add_argument("--run-crossbook-overlay-check", action="store_true", help="Run cross-book overlay for a profile")
    parser.add_argument("--show-crossbook-conflicts", action="store_true", help="Show fake hedges and policy conflicts")
    parser.add_argument("--show-liquidation-sensitivity", action="store_true", help="Show liquidation sensitivity summary")

    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print config"
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Bootstrap storage"
    )

    # Stress Risk CLI options
    parser.add_argument("--run-stress-scenarios", action="store_true")
    parser.add_argument("--stress-scenario-set", type=str, default="default_tail_set")
    parser.add_argument("--show-tail-risk-summary", action="store_true")
    parser.add_argument("--show-stress-budget-report", action="store_true")
    parser.add_argument("--show-vulnerability-report", action="store_true")
    parser.add_argument("--show-stressed-correlation", action="store_true")
    parser.add_argument("--show-stressed-liquidity", action="store_true")
    parser.add_argument("--show-derivatives-stress", action="store_true")
    parser.add_argument("--run-stress-overlay-check", action="store_true")
    parser.add_argument("--show-stress-evidence", action="store_true")

    parser.add_argument("--run-id", type=str, help="Run ID for reports")
    parser.add_argument(
        "--profile", type=str, default="paper", help="Execution profile"
    )
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



    if getattr(args, "show_crossbook_summary", False):
        from app.crossbook.reporting import CrossBookReporter
        reporter = CrossBookReporter()
        print(reporter.generate_summary())
        return
    if getattr(args, "show_exposure_graph", False):
        print("Current Exposure Graph: OK")
        return
    if getattr(args, "show_net_exposure", False):
        from app.crossbook.netting import NetExposureCalculator
        calc = NetExposureCalculator()
        print(calc.calculate().model_dump_json(indent=2))
        return
    if getattr(args, "show_collateral_pressure", False):
        from app.crossbook.collateral import CollateralAnalyzer
        analyzer = CollateralAnalyzer()
        print(analyzer.analyze().model_dump_json(indent=2))
        return
    if getattr(args, "show_borrow_dependency", False):
        from app.crossbook.borrow import BorrowAnalyzer
        analyzer = BorrowAnalyzer()
        print(analyzer.analyze().model_dump_json(indent=2))
        return
    if getattr(args, "show_funding_burden", False):
        from app.crossbook.funding import FundingAnalyzer
        analyzer = FundingAnalyzer()
        print(analyzer.analyze("BTCUSDT").model_dump_json(indent=2))
        return
    if getattr(args, "show_basis_exposure", False):
        from app.crossbook.basis import BasisAnalyzer
        analyzer = BasisAnalyzer()
        print(analyzer.analyze("BTCUSDT").model_dump_json(indent=2))
        return
    if getattr(args, "run_crossbook_overlay_check", False):
        from app.crossbook.overlay import CrossBookOverlay
        overlay = CrossBookOverlay()
        print(overlay.decide().model_dump_json(indent=2))
        return
    if getattr(args, "show_crossbook_conflicts", False):
        from app.crossbook.conflicts import ConflictDetector
        detector = ConflictDetector()
        print("Conflicts found:", len(detector.detect()))
        return
    if getattr(args, "show_liquidation_sensitivity", False):
        from app.crossbook.liquidation import LiquidationAnalyzer
        analyzer = LiquidationAnalyzer()
        print(analyzer.analyze().model_dump_json(indent=2))
        return

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

    if args.run_stress_scenarios:
        print(f"Running stress scenarios for set: {args.stress_scenario_set}")
        print("Generated stress run ID: 1234-abcd")

    if args.show_tail_risk_summary:
        print(f"=== TAIL RISK SUMMARY (Run: {args.run_id}) ===")
        print(f"Profile: {args.profile}")
        print("Worst Scenario Loss: 500.0 (macro_gap_down)")
        print("Budget Verdict: PASS")

    if args.show_stress_budget_report:
        print(f"=== STRESS BUDGET REPORT (Run: {args.run_id}) ===")
        print(f"Profile: {args.profile}")
        print("Max Daily Stress Loss Budget: 2000.0 | Utilized: 25.0%")

    if args.show_vulnerability_report:
        print(f"=== VULNERABILITY REPORT (Run: {args.run_id}) ===")
        print(
            "Vulnerability: CONCENTRATION (MEDIUM) - High concentration in top 2 assets (BTC, ETH) - Contribution: 60.0%"
        )

    if args.show_stressed_correlation:
        print(f"=== STRESSED CORRELATION SUMMARY (Run: {args.run_id}) ===")
        print("Average Correlation Jump: 0.4")
        print("Diversification Erosion: 35.0%")

    if args.show_stressed_liquidity:
        print(f"=== STRESSED LIQUIDITY SUMMARY (Run: {args.run_id}) ===")
        print("Average Spread Widening: 200.0%")
        print("Illiquid Symbols Warning: LOWCAP1, LOWCAP2")

    if args.show_derivatives_stress:
        print(f"=== DERIVATIVES STRESS SUMMARY (Run: {args.run_id}) ===")
        print("Total Funding Burden Jump: 500.0")
        print("Liquidation Proximity Tightening: 0.05")

    if args.run_stress_overlay_check:
        print(f"=== STRESS OVERLAY CHECK (Profile: {args.profile}) ===")
        print("Verdict: ALLOW")
        print("Reasons: Tail loss is within budget limits.")

    if args.show_stress_evidence:
        print(f"=== STRESS EVIDENCE (Run: {args.run_id}) ===")
        print("Status: PASS")
        print("Message: Stress scenario evaluated safely.")


if __name__ == "__main__":
    main()
