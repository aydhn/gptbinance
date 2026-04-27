import sys
import logging
import argparse
import json
import pandas as pd
import numpy as np

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

    # Placeholder flags that would normally query a running instance, but for now we just acknowledge them
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

    # Parse args (we only care about the ones not handled by bootstrap)
    # Using parse_known_args in case other args exist
    args, unknown = parser.parse_known_args()

    # We still need to bootstrap to get config and context
    config, ctx = bootstrap()
    logger = logging.getLogger(__name__)

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

    # Initialize core components here in the future
    if get_notifier:
        notifier = get_notifier(config)
        notifier.send_message(
            f"Application started in {ctx.profile.value} mode. Run ID: {ctx.run_id}"
        )

    logger.info("Main execution block reached. Exiting gracefully.")


if __name__ == "__main__":
    main()
