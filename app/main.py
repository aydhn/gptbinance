import sys
import logging
from app.core.bootstrap import bootstrap
from app.telegram.notifier import get_notifier
from app.ops.smoke_checks import (
    check_binance_connectivity,
    check_time_sync,
    fetch_exchange_info,
    print_symbol_universe,
)


def main():
    # If custom smoke check arguments are provided, handle them here
    # Since we are using standard argparse inside bootstrap.py, we'll extract them there
    # But for a quick CLI without altering bootstrap extensively right now:
    args = sys.argv[1:]

    # We still need to bootstrap to get config and context
    config, ctx = bootstrap()
    logger = logging.getLogger(__name__)

    # Handle Smoke Checks Flags
    if "--check-binance-connectivity" in args:
        check_binance_connectivity(config, ctx.profile)
        sys.exit(0)

    if "--check-time-sync" in args:
        check_time_sync(config, ctx.profile)
        sys.exit(0)

    if "--fetch-exchange-info" in args:
        fetch_exchange_info(config, ctx.profile)
        sys.exit(0)

    if "--print-symbol-universe" in args:
        print_symbol_universe(config, ctx.profile)
        sys.exit(0)

    # Initialize core components here in the future
    notifier = get_notifier(config)
    notifier.send_message(
        f"Application started in {ctx.profile.value} mode. Run ID: {ctx.run_id}"
    )

    logger.info("Main execution block reached. Exiting gracefully.")


if __name__ == "__main__":
    main()
