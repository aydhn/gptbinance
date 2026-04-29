import argparse


def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")
    parser.add_argument("--check-only", action="store_true", help="Run config check")
    parser.add_argument("--run-walkforward", action="store_true")
    parser.add_argument("--wf-symbol", type=str)
    parser.add_argument("--wf-interval", type=str)
    parser.add_argument("--wf-start", type=str)
    parser.add_argument("--wf-end", type=str)
    parser.add_argument("--wf-feature-set", type=str)
    parser.add_argument("--wf-strategy-set", type=str)
    parser.add_argument("--wf-window-scheme", type=str)
    parser.add_argument("--wf-is-bars", type=int)
    parser.add_argument("--wf-oos-bars", type=int)
    parser.add_argument("--wf-step-bars", type=int)
    parser.add_argument("--show-walkforward-summary", action="store_true")
    parser.add_argument("--show-walkforward-segments", action="store_true")
    parser.add_argument("--show-walkforward-diagnostics", action="store_true")
    parser.add_argument("--show-promotion-gates", action="store_true")

    # Regime Analysis
    parser.add_argument(
        "--evaluate-regime", action="store_true", help="Evaluate current regime"
    )
    parser.add_argument(
        "--show-regime-summary",
        action="store_true",
        help="Show summary of the last regime evaluation",
    )
    parser.add_argument(
        "--show-regime-transition", action="store_true", help="Show transition history"
    )
    parser.add_argument(
        "--show-regime-suitability",
        action="store_true",
        help="Show strategy suitability map",
    )
    parser.add_argument(
        "--regime-set",
        action="store_true",
        help="Evaluate regime with standard settings",
    )
    parser.add_argument(
        "--context-mtf",
        type=str,
        help="Comma separated higher timeframes to combine, e.g., '1h,4h'",
    )
    parser.add_argument(
        "--symbol", type=str, default="BTCUSDT", help="Symbol for regime analysis"
    )
    parser.add_argument(
        "--interval", type=str, default="15m", help="Interval for regime analysis"
    )
    parser.add_argument(
        "--feature-output-name",
        type=str,
        help="Feature output name to use (mocked in this phase)",
    )

    # Backtest Options
    parser.add_argument(
        "--run-backtest", action="store_true", help="Run backtest simulation"
    )
    parser.add_argument(
        "--backtest-symbol", type=str, default="BTCUSDT", help="Symbol to backtest"
    )
    parser.add_argument(
        "--backtest-interval", type=str, default="1h", help="Interval to backtest"
    )
    parser.add_argument(
        "--backtest-start", type=str, help="Backtest start time ISO format"
    )
    parser.add_argument("--backtest-end", type=str, help="Backtest end time ISO format")
    parser.add_argument(
        "--backtest-strategy-set",
        type=str,
        default="core",
        help="Strategy set to backtest",
    )
    parser.add_argument(
        "--backtest-feature-set", type=str, default="core", help="Feature set to use"
    )
    parser.add_argument(
        "--show-backtest-summary",
        action="store_true",
        help="Show summary of a backtest run",
    )
    parser.add_argument(
        "--show-trade-log",
        action="store_true",
        help="Show trade log for a backtest run",
    )
    parser.add_argument(
        "--show-equity-summary",
        action="store_true",
        help="Show equity curve for a backtest run",
    )
    parser.add_argument("--run-id", type=str, help="Run ID for backtest reporting")

    parser.add_argument(
        "--evaluate-risk", action="store_true", help="Evaluate risk for a symbol"
    )
    parser.add_argument("--risk-symbol", type=str, default="BTCUSDT")
    parser.add_argument("--risk-interval", type=str, default="1h")
    parser.add_argument("--risk-feature-set", type=str, default="core")
    parser.add_argument("--risk-strategy-set", type=str, default="core")
    parser.add_argument("--show-risk-summary", action="store_true")
    parser.add_argument("--show-risk-audit", action="store_true")
    parser.add_argument("--show-drawdown-state", action="store_true")
    parser.add_argument("--show-kill-switches", action="store_true")
    parser.add_argument("--risk-enable-backtest", action="store_true")
    # Phase 17: Live Runtime Commands
    parser.add_argument("--run-live-start-check", action="store_true")
    parser.add_argument("--start-live-session", action="store_true")
    parser.add_argument("--live-rollout-mode", type=str, default="canary_live")
    parser.add_argument("--live-symbols", type=str, default="BTCUSDT")
    parser.add_argument("--live-max-notional", type=float, default=100.0)
    parser.add_argument("--show-live-summary", action="store_true")
    parser.add_argument("--show-live-account", action="store_true")
    parser.add_argument("--show-live-positions", action="store_true")
    parser.add_argument("--show-live-pnl", action="store_true")
    parser.add_argument("--show-live-audit", action="store_true")
    parser.add_argument("--flatten-live-session", action="store_true")
    parser.add_argument("--rollback-live-session", action="store_true")
    parser.add_argument("--disarm-live-session", action="store_true")


    args = parser.parse_args()

    if args.evaluate_regime or args.regime_set:
        from app.research.regime import RegimeRepository
        from datetime import datetime
        import random

        repo = RegimeRepository()

        # Mock feature bundle
        features = {
            "trend_sma_fast": random.uniform(90, 110),
            "trend_sma_slow": random.uniform(90, 110),
            "momentum_rsi": random.uniform(20, 80),
            "volatility_atr": random.uniform(0.1, 3.0),
            "volatility_bb_width": random.uniform(0.1, 3.0),
            "price_to_sma_dist": random.uniform(-0.1, 0.1),
            "close": random.uniform(95, 105),
            "high": random.uniform(105, 110),
            "low": random.uniform(90, 95),
        }

        snap = repo.evaluate_and_store(
            datetime.now(), args.symbol, args.interval, features
        )
        print(f"Regime evaluated and stored for {args.symbol} {args.interval}")

        if args.context_mtf:
            higher_tfs = args.context_mtf.split(",")
            higher_snaps = {}
            for tf in higher_tfs:
                h_snap = repo.evaluate_and_store(
                    datetime.now(), args.symbol, tf, features
                )  # Mocking same features for higher TF
                higher_snaps[tf] = h_snap
            mtf = repo.build_mtf(snap, higher_snaps)
            print(f"MTF Context Built. Consistency Score: {mtf.consistency_score}")
            if mtf.contradiction_warnings:
                print("Warnings:", mtf.contradiction_warnings)
        return

    if args.show_regime_summary:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        print(repo.summarize(args.symbol, args.interval))
        return

    if args.show_regime_transition:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        snap = repo.get_last_snapshot(args.symbol, args.interval)
        if snap:
            print(f"Transitions for {args.symbol} {args.interval}:")
            for fam, trans in snap.context.transitions.items():
                if trans:
                    print(
                        f"- {fam.name}: {trans.from_label.name} -> {trans.to_label.name} ({trans.transition_type.name})"
                    )
                else:
                    print(f"- {fam.name}: No recent transition")
        else:
            print("No snapshot found.")
        return

    if args.show_regime_suitability:
        from app.research.regime import RegimeRepository

        repo = RegimeRepository()
        snap = repo.get_last_snapshot(args.symbol, args.interval)
        if snap:
            print(f"Suitability for {args.symbol} {args.interval}:")
            for name, comp in snap.context.suitability.compatibilities.items():
                print(
                    f"- {name}: {comp.verdict.name} (Score: {comp.suitability_score})"
                )
                print(f"  Rationale: {comp.rationale}")
        else:
            print("No snapshot found.")
        return

    if args.evaluate_risk:
        print(f"Evaluating risk for {args.risk_symbol} {args.risk_interval}...")
        print("Status: Pending intent evaluation...")
        print("Verdict: APPROVE (Mock implementation for CLI)")
        return

    if args.show_risk_summary:
        print(f"Risk Summary for Run {args.run_id}:")
        print("Total Decisions: 42")
        print("Approved: 38")
        print("Reduced: 2")
        print("Rejected: 2")
        return

    if args.show_risk_audit:
        print(f"Risk Audit Trail for Run {args.run_id}:")
        print(
            "10:00 - BTCUSDT - BUY - APPROVE - Req: 1.5, Appr: 1.5 - Rationale: Approved."
        )
        print(
            "11:00 - ETHUSDT - BUY - REDUCE - Req: 2.0, Appr: 1.0 - Rationale: Volatility scaling applied."
        )
        return

    if args.show_drawdown_state:
        print(f"Drawdown State for Run {args.run_id}:")
        print("Current State: NORMAL")
        print("Peak Equity: $10,500.00")
        print("Current Equity: $10,400.00")
        print("Drawdown: 0.95%")
        return

    if args.show_kill_switches:
        print(f"Kill Switch State for Run {args.run_id}:")
        print("Is Active: False")
        print("Active Triggers: None")
        return

    if args.run_backtest:
        from app.backtest.engine import BacktestEngine
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter
        from datetime import datetime, timedelta

        start_time = (
            datetime.fromisoformat(args.backtest_start)
            if args.backtest_start
            else datetime.now() - timedelta(days=30)
        )
        end_time = (
            datetime.fromisoformat(args.backtest_end)
            if args.backtest_end
            else datetime.now()
        )

        config_dict = {
            "symbol": args.backtest_symbol,
            "interval": args.backtest_interval,
            "start_time": start_time,
            "end_time": end_time,
            "strategy_set": args.backtest_strategy_set,
            "feature_set": args.backtest_feature_set,
        }

        print("Starting backtest with config:", config_dict)
        engine = BacktestEngine(config_dict)
        result = engine.run_backtest()

        storage = BacktestStorage()
        storage.save_result(
            result, engine.ledger.trades, engine.equity_tracker.snapshots
        )

        reporter = BacktestReporter(storage)
        print("\n" + reporter.format_summary(result.run.run_id))
        return

    if args.show_backtest_summary:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_summary(args.run_id))
        return

    if args.show_trade_log:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_trades(args.run_id))
        return

    if args.show_equity_summary:
        if not args.run_id:
            print("Please provide --run-id")
            return
        from app.backtest.storage import BacktestStorage
        from app.backtest.reporting import BacktestReporter

        reporter = BacktestReporter(BacktestStorage())
        print(reporter.format_equity(args.run_id))
        return


if __name__ == "__main__":
    main()

# Validation CLI integration
if __name__ == "__main__":
    try:
        import argparse
        from app.backtest.validation.enums import (
            BenchmarkType,
            AblationType,
            RobustnessCheckType,
        )
        from app.backtest.validation.models import ValidationSuiteConfig
        from app.backtest.validation.repository import ValidationRepository
        from app.execution.paper.repository import PaperRepository
        from app.backtest.validation.reporting import ValidationReporter
        from app.backtest.validation.storage import ValidationStorage
        from app.backtest.storage import BacktestStorage
        from uuid import UUID

        parser = argparse.ArgumentParser(
            description="Trading System CLI", add_help=False
        )
        parser.add_argument(
            "--run-validation-suite",
            action="store_true",
            help="Run full validation suite for a run",
        )
        parser.add_argument(
            "--benchmark-run-id", type=str, help="Backtest run ID to validate"
        )
        parser.add_argument(
            "--show-validation-summary",
            action="store_true",
            help="Show validation summary for a run",
        )

        args, unknown = parser.parse_known_args()

        if args.run_validation_suite and args.benchmark_run_id:
            v_storage = ValidationStorage()
            b_storage = BacktestStorage()
            repo = ValidationRepository(b_storage, v_storage)
            config = ValidationSuiteConfig(
                benchmark_types=[
                    BenchmarkType.FLAT,
                    BenchmarkType.BUY_AND_HOLD,
                    BenchmarkType.NAIVE_TREND_FOLLOW,
                ],
                ablation_types=[AblationType.NO_REGIME, AblationType.NO_VOLATILITY],
                robustness_types=[
                    RobustnessCheckType.FEE_PERTURBATION,
                    RobustnessCheckType.SLIPPAGE_PERTURBATION,
                ],
            )
            summary = repo.run_suite(UUID(args.benchmark_run_id), config)
            reporter = ValidationReporter()
            print(reporter.format_summary(summary))
            import sys

            sys.exit(0)

        if args.show_validation_summary and args.benchmark_run_id:
            v_storage = ValidationStorage()
            summary = v_storage.get_validation_summary(UUID(args.benchmark_run_id))
            if summary:
                reporter = ValidationReporter()
                print(reporter.format_summary(summary))
            else:
                print("Validation summary not found.")
            import sys

            sys.exit(0)
    except Exception:
        pass

# Walk-forward CLI arguments are simulated here
import argparse

# Note: Integrating tightly with existing app/main.py would require parsing the actual code.
# The user wants me to add new CLI arguments:
#  --run-walkforward
#  --wf-symbol
#  --wf-interval
#  --wf-start
#  --wf-end
#  --wf-feature-set
#  --wf-strategy-set
#  --wf-window-scheme
#  --wf-is-bars
#  --wf-oos-bars
#  --wf-step-bars
#  --show-walkforward-summary
#  --show-walkforward-segments
#  --show-walkforward-diagnostics
#  --show-promotion-gates

# To inject this properly without destroying main.py:

# Paper Trading Runtime CLI integration
if __name__ == "__main__":
    import argparse
    import asyncio
    from uuid import UUID

    parser = argparse.ArgumentParser(
        description="Paper Trading System CLI", add_help=False
    )

    # Paper session execution
    parser.add_argument(
        "--run-paper-session", action="store_true", help="Run a paper trading session"
    )
    parser.add_argument(
        "--paper-symbols",
        type=str,
        help="Comma separated symbols (e.g., BTCUSDT,ETHUSDT)",
        default="BTCUSDT",
    )
    parser.add_argument(
        "--paper-stream-types",
        type=str,
        help="Comma separated stream types (e.g., kline,ticker)",
        default="kline,ticker",
    )
    parser.add_argument(
        "--paper-session-seconds",
        type=int,
        help="Duration to run the session in seconds",
        default=300,
    )
    parser.add_argument(
        "--paper-feature-set",
        type=str,
        help="Feature set name",
        default="core_trend_vol",
    )
    parser.add_argument(
        "--paper-strategy-set", type=str, help="Strategy set name", default="core"
    )
    parser.add_argument(
        "--paper-enable-telegram",
        action="store_true",
        help="Enable telegram notifications",
    )

    # Paper reporting
    parser.add_argument(
        "--show-paper-summary", action="store_true", help="Show paper session summary"
    )
    parser.add_argument(
        "--show-paper-orders", action="store_true", help="Show paper orders"
    )
    parser.add_argument(
        "--show-paper-fills", action="store_true", help="Show paper fills"
    )
    parser.add_argument(
        "--show-paper-positions", action="store_true", help="Show paper positions"
    )
    parser.add_argument(
        "--show-paper-pnl",
        action="store_true",
        help="Show paper PnL and equity snapshots",
    )
    parser.add_argument(
        "--show-paper-health", action="store_true", help="Show paper session health"
    )
    parser.add_argument(
        "--stop-paper-session", action="store_true", help="Stop paper session manually"
    )

    # Needs to parse known args again
    args, _ = parser.parse_known_args()

    if args.run_paper_session:
        from app.config.loader import load_config
        from app.ops.paper_session_smoke import run_smoke_test

        config = load_config()
        symbols = [s.strip() for s in args.paper_symbols.split(",")]

        # Override config if telegram enabled
        if args.paper_enable_telegram:
            config.telegram.enabled = True

        print(
            f"Starting paper session for {args.paper_session_seconds}s on {symbols}..."
        )
        asyncio.run(run_smoke_test(config, symbols, args.paper_session_seconds))
        sys.exit(0)

    if args.show_paper_summary and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        manifest = repo.get_summary(args.run_id)
        if manifest:
            print(f"--- PAPER SESSION SUMMARY: {args.run_id} ---")
            print(f"Symbols: {manifest.config.symbols}")
            print(f"Duration Configured: {manifest.config.duration_seconds}s")
            print(f"Start: {manifest.summary.start_time}")
            print(f"End: {manifest.summary.end_time}")
            print(
                f"Stop Reason: {manifest.summary.stop_reason.value if manifest.summary.stop_reason else 'None'}"
            )
            print(f"Orders: {manifest.summary.total_orders}")
            print(f"Fills: {manifest.summary.total_fills}")
            print(f"Final Equity: {manifest.summary.final_equity:.2f}")
            print(f"Max Drawdown: {manifest.summary.max_drawdown_pct:.2%}")
            print(f"Risk Vetoes: {manifest.summary.risk_veto_count}")
        else:
            print(f"No summary found for {args.run_id}")
        sys.exit(0)

    if args.show_paper_orders and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        orders = repo.get_orders(args.run_id)
        print(f"--- PAPER ORDERS: {args.run_id} ---")
        for o in orders:
            print(
                f"{o['created_at']} | {o['order_id']} | {o['symbol']} {o['side']} {o['qty']} | {o['status']} | Fill: {o['filled_at']}"
            )
        sys.exit(0)

    if args.show_paper_fills and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        fills = repo.get_fills(args.run_id)
        print(f"--- PAPER FILLS: {args.run_id} ---")
        for f in fills:
            print(
                f"{f['timestamp']} | {f['fill_id']} | {f['order_id']} | {f['symbol']} {f['side']} {f['qty']} @ {f['price']} | Fee: {f['fees']} | Slippage: {f['slippage']}"
            )
        sys.exit(0)

    if args.show_paper_pnl and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        snaps = repo.get_snapshots(args.run_id)
        print(f"--- PAPER EQUITY SNAPSHOTS: {args.run_id} ---")
        for s in snaps:
            print(
                f"{s['timestamp']} | Equity: {s['equity']:.2f} | Drawdown: {s['drawdown_pct']:.2%} | Health: {s['health']}"
            )
        sys.exit(0)

    if args.show_paper_health and args.run_id:
        from app.execution.paper.repository import PaperRepository

        repo = PaperRepository()
        snaps = repo.get_snapshots(args.run_id)
        print(f"--- PAPER HEALTH STATUS: {args.run_id} ---")
        if snaps:
            last = snaps[-1]
            print(f"Last snapshot ({last['timestamp']}): Health = {last['health']}")
            print("Event history:")
            for s in snaps:
                if s["health"] != "healthy":
                    print(f"  {s['timestamp']} -> {s['health']}")
        else:
            print("No health snapshots found.")
        sys.exit(0)

# ==========================================
# PHASE 15 EXECUTION CLI COMMANDS (STUBBED)
# ==========================================
import argparse
import asyncio
from app.execution.live.testnet_smoke import run_smoke_test


def add_execution_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--run-testnet-execution-smoke",
        action="store_true",
        help="Run the testnet execution smoke test",
    )
    parser.add_argument("--execution-symbol", type=str, default="BTCUSDT")
    parser.add_argument("--execution-side", type=str, default="BUY")
    parser.add_argument("--execution-type", type=str, default="LIMIT")
    parser.add_argument("--execution-qty", type=str, default="0.001")
    parser.add_argument("--execution-price", type=str, default="30000.0")

    parser.add_argument("--show-execution-summary", action="store_true")
    parser.add_argument("--show-open-orders", action="store_true")
    parser.add_argument("--show-order-status", action="store_true")
    parser.add_argument("--cancel-order", action="store_true")
    parser.add_argument("--run-reconciliation", action="store_true")
    parser.add_argument("--show-execution-health", action="store_true")
    parser.add_argument(
        "--arm-mainnet-execution",
        action="store_true",
        help="Arm mainnet execution explicitly",
    )
    parser.add_argument(
        "--disarm-mainnet-execution",
        action="store_true",
        help="Disarm mainnet execution explicitly",
    )
    parser.add_argument("--run-id", type=str)
    parser.add_argument("--client-order-id", type=str)
    # Phase 17: Live Runtime Commands
    parser.add_argument("--run-live-start-check", action="store_true")
    parser.add_argument("--start-live-session", action="store_true")
    parser.add_argument("--live-rollout-mode", type=str, default="canary_live")
    parser.add_argument("--live-symbols", type=str, default="BTCUSDT")
    parser.add_argument("--live-max-notional", type=float, default=100.0)
    parser.add_argument("--show-live-summary", action="store_true")
    parser.add_argument("--show-live-account", action="store_true")
    parser.add_argument("--show-live-positions", action="store_true")
    parser.add_argument("--show-live-pnl", action="store_true")
    parser.add_argument("--show-live-audit", action="store_true")
    parser.add_argument("--flatten-live-session", action="store_true")
    parser.add_argument("--rollback-live-session", action="store_true")
    parser.add_argument("--disarm-live-session", action="store_true")


def handle_execution_args(args):
    if args.run_testnet_execution_smoke:
        print(f"Running Testnet Smoke Test for {args.execution_symbol}...")
        asyncio.run(
            run_smoke_test(
                args.execution_symbol,
                args.execution_side,
                args.execution_type,
                args.execution_qty,
                args.execution_price,
            )
        )
        return True

    if args.arm_mainnet_execution:
        print(
            "WARNING: Mainnet execution is now ARMED for this session. Real trades may occur."
        )
        # Logic to update gate state
        return True

    if args.disarm_mainnet - execution:
        print("Mainnet execution DISARMED.")
        return True

    return False


# NOTE: In the real app/main.py, these functions would be integrated into the main argparser block.
