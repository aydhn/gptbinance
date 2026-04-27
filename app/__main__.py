import sys
import logging
import argparse
import json
from app.core.bootstrap import bootstrap
from app.healthcheck import run_healthcheck

from app.telegram.notifier import get_notifier
from app.ops.smoke_checks import (
    check_binance_connectivity,
    check_time_sync,
    fetch_exchange_info,
    print_symbol_universe,
)
from app.ops.live_stream_smoke import run_live_stream_smoke


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

    # Parse args (we only care about the ones not handled by bootstrap)
    # Using parse_known_args in case other args exist
    args, unknown = parser.parse_known_args()

    # We still need to bootstrap to get config and context
    config, ctx = bootstrap()
    logger = logging.getLogger(__name__)

    if args.healthcheck:
        status = run_healthcheck(config)
        print(json.dumps(status, indent=2))
        sys.exit(0 if status["status"] == "ok" else 1)

    # Handle Smoke Checks Flags
    if args.check_binance_connectivity:
        check_binance_connectivity(config, ctx.profile)
        sys.exit(0)

    if args.check_time_sync:
        check_time_sync(config, ctx.profile)
        sys.exit(0)

    if args.fetch_exchange_info:
        fetch_exchange_info(config, ctx.profile)
        sys.exit(0)

    if args.print_symbol_universe:
        print_symbol_universe(config, ctx.profile)
        sys.exit(0)

    if args.live_stream_smoke:
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

    # Initialize core components here in the future
    notifier = get_notifier(config)
    notifier.send_message(
        f"Application started in {ctx.profile.value} mode. Run ID: {ctx.run_id}"
    )

    logger.info("Main execution block reached. Exiting gracefully.")


if __name__ == "__main__":
    main()
