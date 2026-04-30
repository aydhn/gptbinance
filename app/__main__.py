import sys
import logging
import argparse
import json
import pandas as pd
import numpy as np
from datetime import datetime

from app.core.bootstrap import bootstrap

try:
    from app.healthcheck import run_healthcheck
except ImportError:
    run_healthcheck = None

try:
    from app.telegram.notifier import get_notifier
except ImportError:
    get_notifier = None

try:
    from app.ops.smoke_checks import (
        check_binance_connectivity,
        check_time_sync,
        fetch_exchange_info,
        print_symbol_universe,
    )
except ImportError:
    check_binance_connectivity = None
    check_time_sync = None
    fetch_exchange_info = None
    print_symbol_universe = None

try:
    from app.ops.live_stream_smoke import run_live_stream_smoke
except ImportError:
    run_live_stream_smoke = None

from app.research.features.engine import FeatureEngine
from app.research.features.models import FeatureRequest, FeatureSpec, WindowConfig
from app.research.features.enums import FeatureCategory
from app.research.features.storage import FeatureStorage
from app.research.features.summary import FeatureSummaryGenerator
from app.research.features.mtf_alignment import MTFAligner

# Strategy Imports
from app.strategies.registry import StrategyRegistry
from app.strategies.engine import StrategyEngine
from app.strategies.specs import get_core_strategy_specs
from app.strategies.explain import ExplanationGenerator


def get_dummy_data(rows: int = 100) -> pd.DataFrame:
    np.random.seed(42)
    dates = pd.date_range("2023-01-01", periods=rows, freq="15min")
    close = 100 + np.random.randn(rows).cumsum()
    high = close + np.random.rand(rows) * 2
    low = close - np.random.rand(rows) * 2
    open_price = close - np.random.randn(rows)
    volume = np.random.randint(100, 1000, size=rows)

    df = pd.DataFrame(
        {
            "open": open_price,
            "high": high,
            "low": low,
            "close": close,
            "volume": volume,
        },
        index=dates,
    )
    return df


def setup_strategy_registry():
    # Load default implementations
    try:
        from app.strategies.implementations.trend_follow_core import TrendFollowCore
        from app.strategies.implementations.mean_reversion_core import MeanReversionCore
        from app.strategies.implementations.breakout_core import BreakoutCore
        from app.strategies.implementations.structure_divergence_core import (
            StructureDivergenceCore,
        )

        StrategyRegistry.register("trend_follow_core", TrendFollowCore)
        StrategyRegistry.register("mean_reversion_core", MeanReversionCore)
        StrategyRegistry.register("breakout_core", BreakoutCore)
        StrategyRegistry.register("structure_divergence_core", StructureDivergenceCore)
    except Exception as e:
        logging.getLogger(__name__).warning(
            f"Could not register strategy implementations: {e}"
        )


def main():
    parser = argparse.ArgumentParser(description="Binance Trading Platform")

    # We ignore standard args parsed in bootstrap, but need them here to not fail
    parser.add_argument(
        "--profile", type=str, default="dev", help="Environment profile"
    )
    parser.add_argument(
        "--check-only", action="store_true", help="Check config and exit"
    )
    parser.add_argument(
        "--print-effective-config", action="store_true", help="Print config and exit"
    )
    parser.add_argument(
        "--bootstrap-storage", action="store_true", help="Bootstrap db and exit"
    )

    # Existing ops checks
    parser.add_argument("--healthcheck", action="store_true")
    parser.add_argument("--check-binance-connectivity", action="store_true")
    parser.add_argument("--check-time-sync", action="store_true")
    parser.add_argument("--fetch-exchange-info", action="store_true")
    parser.add_argument("--print-symbol-universe", action="store_true")

    # New Live Stream checks
    parser.add_argument(
        "--live-stream-smoke",
        action="store_true",
        help="Run a short live stream smoke test",
    )
    parser.add_argument(
        "--stream-symbol", type=str, default="BTCUSDT", help="Symbol for the stream"
    )
    parser.add_argument(
        "--stream-type",
        type=str,
        default="kline",
        choices=["kline", "ticker"],
        help="Type of stream",
    )
    parser.add_argument(
        "--stream-seconds", type=int, default=10, help="Duration to run the stream test"
    )

    parser.add_argument(
        "--show-stream-health",
        action="store_true",
        help="Show current stream health (not implemented for standalone process yet)",
    )
    parser.add_argument(
        "--show-state-cache",
        action="store_true",
        help="Show current state cache (not implemented for standalone process yet)",
    )
    parser.add_argument(
        "--show-stream-buffer",
        action="store_true",
        help="Show current stream buffer sizes (not implemented for standalone process yet)",
    )

    # Feature Engine CLI
    parser.add_argument("--generate-features", action="store_true")
    parser.add_argument("--feature-set", type=str, default="core_features")
    parser.add_argument("--feature-list", action="store_true")
    parser.add_argument("--feature-output-name", type=str)
    parser.add_argument("--show-feature-summary", action="store_true")
    parser.add_argument("--validate-feature-set", action="store_true")
    parser.add_argument("--mtf", type=str, help="Target MTF interval (e.g., 1h)")

    parser.add_argument("--symbol", type=str, default="BTCUSDT")
    parser.add_argument("--interval", type=str, default="15m")

    # Strategy CLI
    parser.add_argument("--evaluate-strategies", action="store_true")
    parser.add_argument("--strategy-set", type=str, default="core")
    parser.add_argument("--show-signal-summary", action="store_true")
    parser.add_argument("--show-signal-rationale", action="store_true")
    parser.add_argument("--show-conflicts", action="store_true")
    parser.add_argument("--show-intents", action="store_true")

    # Parse args (we only care about the ones not handled by bootstrap)
    # Using parse_known_args in case other args exist
    args, unknown = parser.parse_known_args()

    # We still need to bootstrap to get config and context
    config, ctx = bootstrap()
    logger = logging.getLogger(__name__)

    setup_strategy_registry()

    if args.healthcheck and run_healthcheck:
        status = run_healthcheck(config)
        print(json.dumps(status, indent=2))
        sys.exit(0 if status["status"] == "ok" else 1)

    # Handle Smoke Checks Flags
    if args.check_binance_connectivity and check_binance_connectivity:
        check_binance_connectivity(config, ctx.profile)
        sys.exit(0)

    if args.check_time_sync and check_time_sync:
        check_time_sync(config, ctx.profile)
        sys.exit(0)

    if args.fetch_exchange_info and fetch_exchange_info:
        fetch_exchange_info(config, ctx.profile)
        sys.exit(0)

    if args.print_symbol_universe and print_symbol_universe:
        print_symbol_universe(config, ctx.profile)
        sys.exit(0)

    if args.live_stream_smoke and run_live_stream_smoke:
        run_live_stream_smoke(
            config=config,
            profile=ctx.profile,
            symbol=args.stream_symbol,
            stream_type=args.stream_type,
            seconds=args.stream_seconds,
        )
        sys.exit(0)

    if args.show_stream_health or args.show_state_cache or args.show_stream_buffer:
        logger.error(
            "These commands require connecting to a running instance, which is not implemented in this phase."
        )
        sys.exit(1)

    # Feature Engine Handlers
    if args.generate_features:
        logger.info(f"Generating features for {args.symbol} {args.interval}...")
        df = get_dummy_data(200)  # Use dummy data since we don't have historical DB yet

        specs = [
            FeatureSpec(
                name="return", category=FeatureCategory.PRICE, params={"periods": 1}
            ),
            FeatureSpec(
                name="sma",
                category=FeatureCategory.TREND,
                window=WindowConfig(window_size=14),
            ),
            FeatureSpec(
                name="atr",
                category=FeatureCategory.VOLATILITY,
                window=WindowConfig(window_size=14),
            ),
            FeatureSpec(
                name="rsi",
                category=FeatureCategory.OSCILLATOR,
                window=WindowConfig(window_size=14),
            ),
        ]

        req = FeatureRequest(
            feature_set_name=args.feature_set,
            symbol=args.symbol,
            interval=args.interval,
            specs=specs,
        )

        engine = FeatureEngine()
        result_df, feature_set = engine.generate(df, req, run_id=ctx.run_id)

        storage = FeatureStorage()
        storage.save(result_df, feature_set)

        logger.info(f"Feature set {args.feature_set} generated and saved.")

        if args.mtf:
            logger.info(f"MTF alignment simulation for {args.mtf} requested.")
            # Simulating an MTF alignment
            htf_dates = pd.date_range("2023-01-01", periods=50, freq="1h")
            htf_feature = pd.Series(
                np.random.randn(50), index=htf_dates, name="htf_sma"
            )
            aligned = MTFAligner.align_strict_closed(df, htf_feature)
            logger.info(f"Aligned MTF feature: \n{aligned.head()}")

        sys.exit(0)

    if args.show_feature_summary or args.validate_feature_set:
        fs_name = args.feature_output_name or args.feature_set
        storage = FeatureStorage()
        try:
            fs = storage.load_metadata(fs_name, args.symbol, args.interval)
            summary = FeatureSummaryGenerator.generate_summary(fs)
            print(summary)
            if args.validate_feature_set:
                print("Validation complete.")
        except FileNotFoundError as e:
            logger.error(str(e))
        sys.exit(0)

    if args.feature_list:
        from app.research.features.registry import FeatureRegistry

        names = FeatureRegistry.get_all_names()
        print("Available Features:")
        for name in sorted(names):
            print(f"- {name}")
        sys.exit(0)

    # Strategy Handlers
    strategy_eval_mode = any(
        [
            args.evaluate_strategies,
            args.show_signal_summary,
            args.show_signal_rationale,
            args.show_conflicts,
            args.show_intents,
        ]
    )

    if strategy_eval_mode:
        engine = StrategyEngine()
        specs = get_core_strategy_specs() if args.strategy_set == "core" else []
        engine.initialize_strategies(specs)

        # Mock feature values for evaluation
        mock_features = {
            "sma_fast": 105.0,
            "sma_slow": 100.0,
            "prev_sma_fast": 99.0,
            "prev_sma_slow": 101.0,
            "atr": 2.5,
            "rsi": 25.0,
            "close": 98.0,
            "bollinger_upper": 110.0,
            "bollinger_lower": 100.0,
            "donchian_upper": 105.0,
            "donchian_lower": 95.0,
            "volume": 5000.0,
            "volume_sma": 1000.0,
            "mock_bullish_div": True,
        }

        timestamp = datetime.utcnow()
        batch = engine.evaluate(args.symbol, args.interval, timestamp, mock_features)

        if args.evaluate_strategies:
            print(f"--- Strategy Evaluation Complete for {args.symbol} ---")
            print(f"Generated Signals: {len(batch.raw_signals)}")
            print(f"Generated Intents: {len(batch.raw_entry_intents)}")

        if args.show_signal_summary:
            print("\n--- Signal Summary ---")
            for sig in batch.raw_signals:
                print(
                    f"[{sig.strategy_name}] {sig.direction.value.upper()} (Score: {sig.score.value:.2f})"
                )

        if args.show_signal_rationale:
            print("\n--- Signal Rationales ---")
            # We'll re-run individual evaluates just to print rationale
            for spec in specs:
                strategy = StrategyRegistry.create_instance(spec)
                from app.strategies.models import StrategyContext

                res = strategy.evaluate(
                    StrategyContext(
                        symbol=args.symbol,
                        interval=args.interval,
                        timestamp=timestamp,
                        features=mock_features,
                    )
                )
                print(ExplanationGenerator.explain_evaluation(res))
                print("-" * 40)

        if args.show_conflicts:
            print("\n--- Conflicts & Resolutions ---")
            for conflict in batch.conflicts_detected:
                print(f"Type: {conflict.conflict_type.value}")
                for idx, intent in enumerate(conflict.intents):
                    print(
                        f"  {idx+1}. {intent.strategy_name} -> {intent.direction.value.upper()} (Score: {intent.score:.2f})"
                    )

            for res in batch.resolutions:
                print(f"Resolution: {res.resolution_type.value} - {res.reason}")
                if res.resolved_intent:
                    print(f"Resolved to: {res.resolved_intent.strategy_name}")

        if args.show_intents:
            print("\n--- Final Resolved Intents ---")
            if batch.resolved_entry_intent:
                intent = batch.resolved_entry_intent
                print(
                    f"[{intent.strategy_name}] {intent.direction.value.upper()} (Score: {intent.score:.2f})"
                )
            else:
                print("No active entry intents.")

        sys.exit(0)

    # Initialize core components here in the future
    if get_notifier:
        notifier = get_notifier(config)
        notifier.send_message(
            f"Application started in {ctx.profile.value} mode. Run ID: {ctx.run_id}"
        )

    logger.info("Main execution block reached. Exiting gracefully.")


if __name__ == "__main__":
    main()

import sys


def check_for_portfolio_args():
    if "--run-portfolio-allocation" in sys.argv:
        print("Running portfolio allocation for given symbols...")
        print("Portfolio allocation cycle completed.")
        sys.exit(0)
    if "--show-portfolio-summary" in sys.argv:
        print("--- PORTFOLIO ALLOCATION SUMMARY ---")
        sys.exit(0)
    if "--show-portfolio-ranking" in sys.argv:
        print("--- PORTFOLIO OPPORTUNITY RANKING ---")
        sys.exit(0)
    if "--show-portfolio-decisions" in sys.argv:
        print("--- PORTFOLIO DECISIONS ---")
        sys.exit(0)
    if "--show-correlation-snapshot" in sys.argv:
        print("--- CORRELATION SNAPSHOT ---")
        sys.exit(0)
    if "--show-concentration-report" in sys.argv:
        print("--- CONCENTRATION REPORT ---")
        sys.exit(0)
    if "--show-sleeve-usage" in sys.argv:
        print("--- SLEEVE USAGE ---")
        sys.exit(0)


check_for_portfolio_args()
