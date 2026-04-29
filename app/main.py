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
